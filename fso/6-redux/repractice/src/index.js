import React from 'react'
import ReactDOM from 'react-dom'
import counterReducer from './reducers/counterReducer'
import { createStore } from 'redux'

const store = createStore(counterReducer)

function App() {
  return (
    <div>
      <div>{store.getState()}</div>
      <button onClick={(e) => store.dispatch({ type: 'INCREMENT' })}>
        plus
      </button>
      <button onClick={(e) => store.dispatch({ type: 'DECREMENT' })}>
        minus
      </button>
      <button onClick={(e) => store.dispatch({ type: 'ZERO' })}>zero</button>
    </div>
  )
}

const renderApp = () =>
  ReactDOM.render(<App />, document.getElementById('root'))

renderApp()
store.subscribe(renderApp)
