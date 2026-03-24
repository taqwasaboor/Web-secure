function Hero() {
  return (
    <section className="hero">

      {/* Live badge */}
      <div className="badge">
        <span className="badge-dot"></span>
        Web Security Scanner
      </div>

      {/* Heading */}
      <h1>
        Scan Your Website.<br />
        <span className="grad">Expose Every Threat.</span>
      </h1>

      {/* Subheading */}
      <p className="hero-sub">
        Run deep reconnaissance with nmap, SSLyze, WebTech and SQLMap — all from one interface. Know your attack surface before attackers do.
      </p>

    </section>
  )
}

export default Hero