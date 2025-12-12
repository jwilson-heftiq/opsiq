import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'OpsIQ',
  description: 'OpsIQ Walking Skeleton',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50">
        <div className="container mx-auto px-4 py-8">
          <header className="mb-8">
            <h1 className="text-3xl font-bold text-gray-900">OpsIQ</h1>
          </header>
          <main>{children}</main>
        </div>
      </body>
    </html>
  )
}

