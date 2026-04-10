import { useState } from 'react'

function ScanCard({ onResults }) {
  // stores what the user types in the input
  const [target, setTarget] = useState('')

  // tracks if scan is currently running
  const [loading, setLoading] = useState(false)

  // handles the scan button click
  const handleScan = async () => {
    if (!target) return
    setLoading(true)
    onResults(null) // clear previous results

    // sends target as JSON body instead of URL path to avoid slash issues
    const response = await fetch('http://127.0.0.1:8000/scan', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' }, // tell server we're sending JSON
      body: JSON.stringify({ target }) // wrap target in object
    })
    const data = await response.json()

    onResults(data) // send results up to App
    setLoading(false)
  }

  return (
    <div className="scan-card glass">
      <p className="scan-label">→ Target URL or IP address</p>

      {/* input row */}
      <div className="scan-row">
        <input
          className="scan-input"
          type="text"
          placeholder="https://example.com  or  192.168.1.1"
          value={target}
          onChange={(e) => setTarget(e.target.value)} // update target as user types
        />
        {/* run scan button */}
        <button className="scan-btn" onClick={handleScan} disabled={loading}>
          {loading ? 'Scanning...' : '⟩ Run Scan'}
        </button>
      </div>

      {/* progress bar shown while scanning */}
      {loading && (
        <div className="progress-bar">
          <div className="progress-fill"></div>
        </div>
      )}
    </div>
  )
}

export default ScanCard