'use client'

import { motion } from 'framer-motion'

type ButtonVariant = 'primary' | 'secondary' | 'ghost'
type ButtonSize = 'sm' | 'md' | 'lg'

interface ButtonProps {
  children: React.ReactNode
  personality: string
  variant?: ButtonVariant
  size?: ButtonSize
  disabled?: boolean
  loading?: boolean
}

const springTransition = {
  type: "spring",
  stiffness: 300,
  damping: 20,
}

export function Button({ 
  children, 
  personality, 
  variant = 'primary', 
  size = 'md',
  disabled = false,
  loading = false 
}: ButtonProps) {
  const sizeStyles = {
    sm: { padding: '8px 16px', fontSize: '14px' },
    md: { padding: '12px 24px', fontSize: '16px' },
    lg: { padding: '16px 32px', fontSize: '18px' },
  }

  const variantStyles = {
    primary: {
      backgroundColor: 'var(--color-accent)',
      color: 'var(--color-secondary)',
    },
    secondary: {
      backgroundColor: 'var(--color-surface)',
      color: 'var(--color-foreground)',
      border: '1px solid var(--color-muted)',
    },
    ghost: {
      backgroundColor: 'transparent',
      color: 'var(--color-foreground)',
    },
  }

  return (
    <motion.button
      whileHover={{ scale: disabled ? 1 : 1.02 }}
      whileTap={{ scale: disabled ? 1 : 0.98 }}
      transition={springTransition}
      disabled={disabled || loading}
      style={{
        ...sizeStyles[size],
        ...variantStyles[variant],
        borderRadius: '8px',
        border: variant !== 'primary' ? '1px solid var(--color-muted)' : 'none',
        fontWeight: 500,
        cursor: disabled ? 'not-allowed' : 'pointer',
        opacity: disabled ? 0.5 : 1,
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '8px',
        transition: 'all 0.15s ease',
      }}
    >
      {loading && (
        <motion.span
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
          style={{
            width: '16px',
            height: '16px',
            border: '2px solid currentColor',
            borderTopColor: 'transparent',
            borderRadius: '50%',
          }}
        />
      )}
      {children}
    </motion.button>
  )
}