#!/usr/bin/env python3
"""
OpenAgent UX - Messenger
Handles inter-agent communication via message passing.
"""

import asyncio
import json
import os
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Callable


class MessageType(Enum):
    REQUEST = "request"
    RESPONSE = "response"
    EVENT = "event"
    ERROR = "error"
    ACK = "ack"


class MessagePriority(Enum):
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class Message:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: MessageType = MessageType.REQUEST
    from_agent: str = ""
    to_agent: str = ""
    action: str = ""
    payload: dict = field(default_factory=dict)
    priority: MessagePriority = MessagePriority.NORMAL
    reply_to: str = ""
    context: dict = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    correlation_id: str = ""


class Messenger:
    def __init__(self, workspace_path: str = "workspace"):
        self.workspace_path = Path(workspace_path)
        self.threads_path = self.workspace_path / "threads"
        self.handlers: dict[str, Callable] = {}
        
    def send_message(
        self,
        to_agent: str,
        from_agent: str,
        action: str,
        payload: dict = None,
        priority: MessagePriority = MessagePriority.NORMAL,
        context: dict = None
    ) -> Message:
        """Send a message to another agent."""
        message = Message(
            type=MessageType.REQUEST,
            from_agent=from_agent,
            to_agent=to_agent,
            action=action,
            payload=payload or {},
            priority=priority,
            context=context or {}
        )
        
        # Store message in thread
        self.store_message(message)
        
        # If in same process, dispatch directly
        if to_agent in self.handlers:
            handler = self.handlers[to_agent]
            asyncio.create_task(self._dispatch_handler(handler, message))
        
        return message
    
    def reply_to(
        self,
        original_message: Message,
        payload: dict,
        success: bool = True
    ) -> Message:
        """Reply to a message."""
        reply = Message(
            type=MessageType.RESPONSE if success else MessageType.ERROR,
            from_agent= original_message.to_agent,
            to_agent=original_message.from_agent,
            action=f"{original_message.action}_result",
            payload=payload,
            reply_to=original_message.id,
            correlation_id=original_message.correlation_id or original_message.id
        )
        
        self.store_message(reply)
        return reply
    
    def broadcast_event(
        self,
        from_agent: str,
        event_type: str,
        payload: dict = None
    ) -> Message:
        """Broadcast an event to all agents."""
        message = Message(
            type=MessageType.EVENT,
            from_agent=from_agent,
            to_agent="*",
            action=event_type,
            payload=payload or {}
        )
        
        self.store_message(message)
        return message
    
    def store_message(self, message: Message):
        """Store message in thread history."""
        thread_file = self.threads_path / f"{message.to_agent}.jsonl"
        thread_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(thread_file, 'a') as f:
            f.write(json.dumps({
                "id": message.id,
                "type": message.type.value,
                "from": message.from_agent,
                "to": message.to_agent,
                "action": message.action,
                "payload": message.payload,
                "timestamp": message.timestamp
            }) + "\n")
    
    def get_thread(self, agent_name: str, limit: int = 50) -> list[Message]:
        """Get message history for an agent."""
        thread_file = self.threads_path / f"{agent_name}.jsonl"
        
        if not thread_file.exists():
            return []
        
        messages = []
        with open(thread_file, 'r') as f:
            for line in f:
                data = json.loads(line)
                messages.append(Message(
                    id=data.get('id', ''),
                    type=MessageType(data.get('type', 'request')),
                    from_agent=data.get('from', ''),
                    to_agent=data.get('to', ''),
                    action=data.get('action', ''),
                    payload=data.get('payload', {}),
                    timestamp=data.get('timestamp', '')
                ))
        
        return messages[-limit:]
    
    def register_handler(self, agent_name: str, handler: Callable):
        """Register a message handler for an agent."""
        self.handlers[agent_name] = handler
    
    async def _dispatch_handler(self, handler: Callable, message: Message):
        """Dispatch a message to its handler."""
        try:
            result = await handler(message)
            if message.reply_to:
                self.reply_to(message, {"result": result}, success=True)
        except Exception as e:
            if message.reply_to:
                self.reply_to(message, {"error": str(e)}, success=False)
    
    def delegate_task(
        self,
        from_agent: str,
        to_agent: str,
        task: str,
        requirements: dict,
        context: dict = None
    ) -> Message:
        """Delegate a task to another agent."""
        return self.send_message(
            to_agent=to_agent,
            from_agent=from_agent,
            action=task,
            payload={
                "task": task,
                "requirements": requirements,
                "context": context or {}
            },
            priority=MessagePriority.HIGH
        )
    
    def get_pending_tasks(self, agent_name: str) -> list[Message]:
        """Get pending messages for an agent."""
        thread = self.get_thread(agent_name)
        return [m for m in thread if m.to_agent == agent_name and m.type == MessageType.REQUEST]


class AgentCommunicator:
    """Helper for agents to communicate."""
    
    def __init__(self, agent_name: str, messenger: Messenger):
        self.agent_name = agent_name
        self.messenger = messenger
    
    def delegate_to(self, agent: str, task: str, **kwargs) -> Message:
        """Delegate a task to another agent."""
        return self.messenger.delegate_task(
            from_agent=self.agent_name,
            to_agent=agent,
            task=task,
            requirements=kwargs
        )
    
    def ask_design(self, task: str, **kwargs) -> Message:
        """Delegate to design lead."""
        return self.delegate_to("design-lead", task, **kwargs)
    
    def ask_frontend(self, task: str, **kwargs) -> Message:
        """Delegate to frontend lead."""
        return self.delegate_to("frontend-lead", task, **kwargs)
    
    def ask_backend(self, task: str, **kwargs) -> Message:
        """Delegate to backend lead."""
        return self.delegate_to("backend-lead", task, **kwargs)
    
    def ask_qa(self, task: str, **kwargs) -> Message:
        """Delegate to QA lead."""
        return self.delegate_to("qa-lead", task, **kwargs)
    
    def broadcast(self, event: str, **kwargs) -> Message:
        """Broadcast an event."""
        return self.messenger.broadcast_event(
            from_agent=self.agent_name,
            event_type=event,
            payload=kwargs
        )


def create_communicator(agent_name: str) -> AgentCommunicator:
    """Factory function to create an agent communicator."""
    messenger = Messenger()
    return AgentCommunicator(agent_name, messenger)
