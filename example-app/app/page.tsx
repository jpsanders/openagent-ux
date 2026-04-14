'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Hero } from '@/components/Hero'
import { Button } from '@/components/Button'
import { Card } from '@/components/Card'
import { Navigation } from '@/components/Navigation'
import { PersonalitySwitcher } from '@/components/PersonalitySwitcher'

type Personality = 'swiss' | 'editorial' | 'tech-noir' | 'playful' | 'minimal' | 'contemporary'

const personalities = [
  { id: 'swiss', name: 'Swiss', description: 'Precision, high contrast, professional' },
  { id: 'editorial', name: 'Editorial', description: 'Sophisticated, timeless, curated' },
  { id: 'tech-noir', name: 'Tech Noir', description: 'Dark, technical, cutting-edge' },
  { id: 'playful', name: 'Playful', description: 'Friendly, energetic, memorable' },
  { id: 'minimal', name: 'Minimal', description: 'Essential, gallery-quality' },
  { id: 'contemporary', name: 'Contemporary', description: 'Bold, current, expressive' },
]

export default function Home() {
  const [personality, setPersonality] = useState<Personality>('swiss')

  return (
    <div data-personality={personality} style={{ minHeight: '100vh' }}>
      <Navigation personality={personality} />
      
      <PersonalitySwitcher
        personalities={personalities}
        current={personality}
        onChange={(id) => setPersonality(id as Personality)}
      />

      <main className="container">
        <AnimatePresence mode="wait">
          <motion.div
            key={personality}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.3 }}
            style={{ paddingTop: '120px' }}
          >
            {/* Hero Section */}
            <section style={{ padding: '60px 0' }}>
              <Hero 
                title={getHeroTitle(personality)}
                subtitle={getHeroSubtitle(personality)}
                personality={personality}
              />
            </section>

            {/* Features Grid */}
            <section style={{ padding: '60px 0' }}>
              <h2 style={{ marginBottom: '32px', fontSize: '28px' }}>
                Design System Preview
              </h2>
              <div style={{ 
                display: 'grid', 
                gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', 
                gap: '24px' 
              }}>
                {personalities.slice(0, 3).map((p) => (
                  <Card key={p.id} personality={personality}>
                    <h3 style={{ marginBottom: '12px' }}>{p.name}</h3>
                    <p style={{ color: 'var(--color-muted)', marginBottom: '16px' }}>
                      {p.description}
                    </p>
                    <Button personality={personality} variant="primary">
                      Get Started
                    </Button>
                  </Card>
                ))}
              </div>
            </section>

            {/* Color Palette Preview */}
            <section style={{ padding: '60px 0' }}>
              <h2 style={{ marginBottom: '32px', fontSize: '28px' }}>
                Color Palette: {personalities.find(p => p.id === personality)?.name}
              </h2>
              <div style={{ display: 'flex', gap: '16px', flexWrap: 'wrap' }}>
                {getColors(personality).map((color, i) => (
                  <div key={i} style={{ textAlign: 'center' }}>
                    <div style={{
                      width: '80px',
                      height: '80px',
                      backgroundColor: color,
                      borderRadius: '12px',
                      border: '1px solid var(--color-muted)',
                      marginBottom: '8px'
                    }} />
                    <span style={{ fontSize: '12px', color: 'var(--color-muted)' }}>
                      {getColorNames(personality)[i]}
                    </span>
                  </div>
                ))}
              </div>
            </section>

            {/* Component Demo */}
            <section style={{ padding: '60px 0' }}>
              <h2 style={{ marginBottom: '32px', fontSize: '28px' }}>
                Component States
              </h2>
              <div style={{ display: 'flex', gap: '24px', flexWrap: 'wrap', alignItems: 'flex-start' }}>
                <div>
                  <h4 style={{ marginBottom: '16px' }}>Buttons</h4>
                  <div style={{ display: 'flex', gap: '12px', flexDirection: 'column' }}>
                    <Button personality={personality} variant="primary">Primary</Button>
                    <Button personality={personality} variant="secondary">Secondary</Button>
                    <Button personality={personality} variant="ghost">Ghost</Button>
                  </div>
                </div>
                <div>
                  <h4 style={{ marginBottom: '16px' }}>Sizes</h4>
                  <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
                    <Button personality={personality} variant="primary" size="sm">Small</Button>
                    <Button personality={personality} variant="primary" size="md">Medium</Button>
                    <Button personality={personality} variant="primary" size="lg">Large</Button>
                  </div>
                </div>
              </div>
            </section>

            {/* Code Example */}
            <section style={{ padding: '60px 0' }}>
              <h2 style={{ marginBottom: '32px', fontSize: '28px' }}>
                Using Your Brand
              </h2>
              <div style={{
                backgroundColor: 'var(--color-surface)',
                padding: '24px',
                borderRadius: '12px',
                fontFamily: 'var(--font-mono)',
                fontSize: '14px',
                overflow: 'auto'
              }}>
                <pre style={{ margin: 0 }}>
{`// After running /brand and choosing ${personality}
// All components automatically use your brand values:

import { Button } from '@/components/Button'

// Uses ${getColors(personality)[2]} as accent
// Uses ${getFontPair(personality)} fonts
// Uses matched spring animation
export function MyComponent() {
  return (
    <Button personality="${personality}">
      Click me
    </Button>
  )
}`}
                </pre>
              </div>
            </section>
          </motion.div>
        </AnimatePresence>
      </main>

      {/* Footer */}
      <footer style={{
        borderTop: '1px solid var(--color-surface)',
        padding: '48px 0',
        marginTop: '80px'
      }}>
        <div className="container" style={{ textAlign: 'center' }}>
          <p style={{ color: 'var(--color-muted)' }}>
            built with openagent-ux | The anti-slop website builder
          </p>
        </div>
      </footer>
    </div>
  )
}

function getHeroTitle(personality: string): string {
  const titles: Record<string, string> = {
    swiss: 'Precision Engineered',
    editorial: 'Crafted for Impact',
    tech_noir: 'Built Different',
    playful: 'Make It Memorable',
    minimal: 'Essential by Design',
    contemporary: 'Boldly Forward',
  }
  return titles[personality] || 'Premium Websites'
}

function getHeroSubtitle(personality: string): string {
  const subtitles: Record<string, string> = {
    swiss: 'Professional websites that perform.',
    editorial: 'Timeless design for modern brands.',
    technical: 'For developers who demand excellence.',
    playful: 'Websites that bring joy.',
    minimal: 'Less noise, more signal.',
    contemporary: 'The future of web design.',
  }
  return subtitles[personality] || 'Unique premium websites'
}

function getColors(personality: string): string[] {
  const colors: Record<string, string[]> = {
    swiss: ['#000000', '#ffffff', '#ff4d00', '#f5f5f5', '#737373'],
    editorial: ['#2d2a26', '#fdfaf6', '#c4704b', '#f5f0e8', '#6b6560'],
    tech_noir: ['#0a0a0a', '#161616', '#00d9ff', '#00d9ff', '#a1a1a1'],
    playful: ['#2d2d2d', '#ffffff', '#ff6b6b', '#4ecdc4', '#a1a1a1'],
    minimal: ['#1a1a1a', '#fafafa', '#1a1a1a', '#e5e5e5', '#a1a1a1'],
    contemporary: ['#1a1a1a', '#ffffff', '#ff3366', '#00ff99', '#6b6560'],
  }
  return colors[personality] || colors.swiss
}

function getColorNames(personality: string): string[] {
  return ['primary', 'background', 'accent', 'surface', 'muted']
}

function getFontPair(personality: string): string {
  const pairs: Record<string, string> = {
    swiss: 'Geist + Fraunces',
    editorial: 'Playfair Display + Source Sans',
    tech_noir: 'Geist + Geist Mono',
    playful: 'Outfit + Nunito',
    minimal: 'Satoshi + General Sans',
    contemporary: 'Syne + DM Sans',
  }
  return pairs[personality] || 'Geist + Fraunces'
}