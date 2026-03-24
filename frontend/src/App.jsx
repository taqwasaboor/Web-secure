import { useState } from 'react'
import './App.css'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import BgOrbs from './components/BgOrbs'
import ScanCard from './components/ScanCard'
import Results from './components/Results'
import ToolsGrid from './components/ToolsGrid' // import tools grid section
import Footer from './components/Footer' // import footer component
function App() {
  // tracks whether light mode is active
  const [isLight, setIsLight] = useState(false)

  // stores scan results to pass down to Results component
  const [scanResults, setScanResults] = useState(null)

  // toggles light/dark class on the root element
  const toggleTheme = () => {
    setIsLight(!isLight)
    document.documentElement.classList.toggle('light')
  }

  return (
    <div>
      {/* animated background orbs */}
      <BgOrbs isLight={isLight} />

      {/* navbar component */}
      <Navbar isLight={isLight} toggleTheme={toggleTheme} />

      {/* main content */}
      <main className="wrapper">
        {/* hero section */}
        <Hero />
        <ToolsGrid /> {/* tools grid showing scanner modules */}

        {/* scan input card — passes results up to App */}
        <ScanCard onResults={setScanResults} />

        {/* results section — shown after scan completes */}
        <Results data={scanResults} />
      </main>
      <Footer /> {/* footer with credit */}
      
    </div>
  )
}

export default App