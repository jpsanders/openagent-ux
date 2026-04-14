'use client'

import { motion } from 'framer-motion'

interface NavigationProps {
  personality: string
}

export function Navigation({ personality }: NavigationProps) {
  return (
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.3 }}
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        zIndex: 100,
        backgroundColor: 'var(--color-background)',
        borderBottom: '1px solid var(--color-surface)',
        backdropFilter: 'blur(10px)',
        backgroundColor: 'rgba(var(--color-background), 0.9)',
      }}
    >
      <div className="container" style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        height: '72px',
      }}>
        <motion.div
          whileHover={{ scale: 1.02 }}
          style={{
            fontSize: '20px',
            fontWeight: 700,
            fontFamily: 'var(--font-heading)',
            cursor: 'pointer',
          }}
        >
          openagent-ux
        </motion.div>
        
        <div style={{ display: 'flex', gap: '32px' }}>
          {['Features', 'Pricing', 'Docs', 'GitHub'].map((item) => (
            <motion.a
              key={item}
              href="#"
              whileHover={{ y: -2 }}
              style={{
                color: 'var(--color-foreground)',
                fontSize: '14px',
                fontWeight: 500,
                opacity: 0.7,
                transition: 'opacity 0.2s',
              }}
            >
              {item}
            </motion.a>
          ))}
        </div>
        
        <div style={{ display: 'flex', gap: '12px' }}>
          <button className="btn" style={{
            backgroundColor: 'transparent',
            color: 'var(--color-foreground)',
            fontSize: '14px',
          }}>
            Sign In
          </button>
          <button className="btn btn-primary" style={{
            fontSize: '14px',
          }}>
            Get Started
          </button>
        </div>
      </div>
    </motion.nav>
  )
}