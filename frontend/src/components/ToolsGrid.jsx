const tools = [
  {
    name: "Nmap",
    icon: "🔍",
    description: "Port scanning and service detection across common network ports.", // tool info shown in card
  },
  {
    name: "SQLMap",
    icon: "🛢️",
    description: "Automated SQL injection detection and database fingerprinting.", // tool info shown in card
  },
  {
    name: "SSLyze",
    icon: "🔒",
    description: "SSL/TLS configuration analysis and certificate validation.", // tool info shown in card
  },
  {
    name: "WebTech",
    icon: "🌐",
    description: "Technology fingerprinting to identify frameworks and libraries.", // tool info shown in card
  },
]

function ToolsGrid() {
  return (
    <section className="tools-section"> {/* tools grid wrapper */}
      <h2 className="tools-title">Powered By</h2>
      <div className="tools-grid"> {/* grid container for tool cards */}
        {tools.map((tool) => ( // loop through each tool
          <div className="tool-card" key={tool.name}> {/* individual tool card */}
            <span className="tool-icon">{tool.icon}</span> {/* emoji icon */}
            <h3 className="tool-name">{tool.name}</h3> {/* tool name */}
            <p className="tool-desc">{tool.description}</p> {/* tool description */}
          </div>
        ))}
      </div>
    </section>
  )
}

export default ToolsGrid