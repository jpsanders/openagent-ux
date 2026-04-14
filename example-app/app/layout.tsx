import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'openagent-ux | Premium AI Website Builder',
  description: 'AI-powered frontend builder that creates UNIQUE, premium websites - NOT generic AI slop.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>{children}</body>
    </html>
  )
}