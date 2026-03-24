function Results({ data }) {
  // if no data yet, show nothing
  if (!data) return null

  return (
    <div className="results-section">
      <p className="section-title">Scan Results — {data.target}</p>

      <div className="results-grid">

        {/* Nmap results card */}
        {data.nmap && (
          <div className={`result-card glass ${data.nmap.error ? 'warning' : 'info'}`}>
            <div className="result-header">
              <div>
                <div className="result-title">🗺 Nmap Port Scan</div>
                <span className={`result-tag ${data.nmap.error ? 'tag-warning' : 'tag-info'}`}>
                  {data.nmap.error ? 'Error' : `${data.nmap.ports?.length} ports found`}
                </span>
              </div>
            </div>
            {/* show error or list of ports */}
            {data.nmap.error ? (
              <p className="result-desc">{data.nmap.error}</p>
            ) : (
              <div className="port-list">
                {data.nmap.ports?.map((p) => (
                  <div key={p.port} className={`port-item severity-${p.severity}`}>
                    <span className="port-num">{p.port}/tcp</span>
                    <span className="port-service">{p.service}</span>
                    <span className={`result-tag tag-${p.severity}`}>{p.severity}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {/* SSLyze results card */}
        {data.sslyze && (
          <div className={`result-card glass ${data.sslyze.error ? 'warning' : 'safe'}`}>
            <div className="result-header">
              <div>
                <div className="result-title">🔐 SSL/TLS Analysis</div>
                <span className={`result-tag ${data.sslyze.error ? 'tag-warning' : 'tag-safe'}`}>
                  {data.sslyze.error ? 'Error' : 'Passed'}
                </span>
              </div>
            </div>
            <p className="result-desc">
              {data.sslyze.error ? data.sslyze.error : JSON.stringify(data.sslyze)}
            </p>
          </div>
        )}

        {/* WebTech results card */}
        {data.webtech && (
          <div className={`result-card glass ${data.webtech.error ? 'warning' : 'info'}`}>
            <div className="result-header">
              <div>
                <div className="result-title">📡 Technology Stack</div>
                <span className={`result-tag ${data.webtech.error ? 'tag-warning' : 'tag-info'}`}>
                  {data.webtech.error ? 'Error' : 'Detected'}
                </span>
              </div>
            </div>
            <p className="result-desc">
              {data.webtech.error ? data.webtech.error : data.webtech.technologies}
            </p>
          </div>
        )}

      </div>
    </div>
  )
}

export default Results