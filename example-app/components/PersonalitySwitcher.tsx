'use client'

import { motion } from 'framer-motion'

interface Personality {
  id: string
  name: string
  description: string
}

interface PersonalitySwitcherProps {
  personalities: Personality[]
  current: string
  onChange: (id: string) => void
}

export function PersonalitySwitcher({ personalities, current, onChange }: PersonalitySwitcherProps) {
  return (
    <div style={{
      position: 'fixed',
      bottom: '24px',
      left: '50%',
      transform: 'translateX(-50%)',
      zIndex: 50,
      backgroundColor: 'var(--color-surface)',
      borderRadius: '16px',
      padding: '12px',
      display: 'flex',
      gap: '8px',
      boxShadow: '0 8px 32px rgba(0, 0, 0, 0.15)',
      border: '1px solid var(--color-muted)',
    }}>
      {personalities.map((p) => (
        <motion.button
          key={p.id}
          onClick={() => onChange(p.id)}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          style={{
            padding: '10px 16px',
            fontSize: '13px',
            fontWeight: 500,
            borderRadius: '8px',
            border: 'none',
            cursor: 'pointer',
            backgroundColor: current === p.id ? 'var(--color-accent)' : 'transparent',
            color: current === p.id ? 'var(--color-secondary)' : 'var(--color-foreground)',
            opacity: current === p.id ? 1 : 0.7,
            transition: 'all 0.2s ease',
            fontFamily: 'var(--font-body)',
          }}
        >
          {p.name}
        </motion.button>
      ))}
    </div>
  )
}