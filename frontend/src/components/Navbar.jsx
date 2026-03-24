function Navbar({ isLight, toggleTheme }) {
  return (
    <nav className="nav">
      <div className="wrapper">
        <div className="nav-inner glass">

          {/* Logo */}
          <div className="logo">
            <div className="logo-icon">⬡</div>
            WebSecure
          </div>

          {/* Right side: links + theme toggle */}
          <div className="nav-right">
            <ul className="nav-links">
              <li><a href="#">Docs</a></li>
              <li><a href="#">GitHub</a></li>
            </ul>

            {/* Theme toggle button */}
            <button className="theme-toggle" onClick={toggleTheme}>
              {isLight ? '🌙' : '☀️'}
            </button>
          </div>

        </div>
      </div>
    </nav>
  )
}

export default Navbar