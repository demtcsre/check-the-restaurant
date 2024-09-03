import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [API, setAPI] = useState([])

  const fetchAPI = async () => {
    const response = await axios.get("http://127.0.0.1:5000/")
  }
  
  return (
    <>
    </>
  )
}

export default App
