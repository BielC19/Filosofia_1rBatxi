import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Big Data ODS</h1>
      <div className="card">
        T'agrada? 
        <button onClick={() => setCount((count) => count + 1)}>
          Si {count}
        </button>
        <p>
          Biel Costa, Hugo Martin i Genis Baños
        </p>
      </div>

    </>
  )
}

export default App
