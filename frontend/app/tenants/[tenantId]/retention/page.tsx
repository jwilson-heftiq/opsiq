'use client'

import { use, useEffect, useState } from 'react'

interface RetentionSummary {
  total_shoppers: number;
  total_trips_last_30_days: number;
}

export default function RetentionPage({
  params,
}: {
  params: Promise<{ tenantId: string }>
}) {
  const { tenantId } = use(params)
  const [summary, setSummary] = useState<RetentionSummary | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        setLoading(true)
        const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000'
        const response = await fetch(
          `${backendUrl}/tenants/${tenantId}/retention/summary`
        )
        
        if (!response.ok) {
          throw new Error(`Failed to fetch: ${response.statusText}`)
        }
        
        const data = await response.json()
        setSummary(data)
        setError(null)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error')
        setSummary(null)
      } finally {
        setLoading(false)
      }
    }

    fetchSummary()
  }, [tenantId])

  if (loading) {
    return (
      <div className="max-w-2xl">
        <h2 className="text-2xl font-semibold text-gray-800 mb-4">
          Retention Summary - {tenantId}
        </h2>
        <p className="text-gray-600">Loading...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="max-w-2xl">
        <h2 className="text-2xl font-semibold text-gray-800 mb-4">
          Retention Summary - {tenantId}
        </h2>
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <p className="text-red-800">Error: {error}</p>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-2xl">
      <h2 className="text-2xl font-semibold text-gray-800 mb-6">
        Retention Summary - {tenantId}
      </h2>
      
      {summary && (
        <div className="bg-white rounded-lg shadow p-6 space-y-4">
          <div>
            <h3 className="text-sm font-medium text-gray-500">Total Shoppers</h3>
            <p className="text-3xl font-bold text-gray-900">{summary.total_shoppers}</p>
          </div>
          
          <div>
            <h3 className="text-sm font-medium text-gray-500">Total Trips (Last 30 Days)</h3>
            <p className="text-3xl font-bold text-gray-900">{summary.total_trips_last_30_days}</p>
          </div>
        </div>
      )}
    </div>
  )
}

