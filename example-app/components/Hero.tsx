'use client'

import { motion } from 'framer-motion'

interface HeroProps {
  title: string
  subtitle: string
  personality: string
}

export function Hero({ title, subtitle, personality }: HeroProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      style={{ textAlign: 'center', maxWidth: '800px', margin: '0 auto' }}
    >
      <motion.h1
        style={{
          fontSize: 'clamp(2.5rem, 5vw, 4rem)',
          fontWeight: 700,
          marginBottom: '16px',
          lineHeight: 1.1,
        }}
      >
        {title}
      </motion.h1>
      <motion.p
        style={{
          fontSize: 'clamp(1.125rem, 2vw, 1.5rem)',
          color: 'var(--color-muted)',
          marginBottom: '32px',
        }}
      >
        {subtitle}
      </motion.p>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.3 }}
        style={{ display: 'flex', gap: '16px', justifyContent: 'center', flexWrap: 'wrap' }}
      >
        <button
          className="btn btn-primary"
          style={{
            padding: '16px 32px',
            fontSize: '16px',
          }}
        >
          Get Started
        </button>
        <button
          className="btn"
          style={{
            backgroundColor: 'var(--color-surface)',
            color: 'var(--color-foreground)',
            padding: '16px 32px',
            fontSize: '16px',
          }}
        >
          View Demo
        </button>
      </motion.div>
    </motion.div>
  )
}