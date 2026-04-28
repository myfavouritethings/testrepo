import { useState, useEffect } from 'react'
import './App.css'
import HealthCheck from './components/HealthCheck'

function App() {
  return (
    <>
      <h1>Budget App</h1>
      <div className="card">
        <HealthCheck />
      </div>
    </>
  )
}

export default App
