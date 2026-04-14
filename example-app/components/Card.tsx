'use client'

import { motion } from 'framer-motion'

interface CardProps {
  children: React.ReactNode
  personality: string
  interactive?: boolean
}

export function Card({ children, personality, interactive = true }: CardProps) {
  if (interactive) {
    return (
      <motion.div
        whileHover={{ y: -4, boxShadow: '0 12px 32px rgba(0, 0, 0, 0.1)' }}
        whileTap={{ scale: 0.98 }}
        transition={{ type: 'spring', stiffness: 300, damping: 20 }}
        style={{
          backgroundColor: 'var(--color-surface)',
          borderRadius: '12px',
          padding: '24px',
          cursor: 'pointer',
        }}
      >
        {children}
      </motion.div>
    )
  }

  return (
    <div
      style={{
        backgroundColor: 'var(--color-surface)',
        borderRadius: '12px',
        padding: '24px',
      }}
    >
      {children}
    </div>
  )
}