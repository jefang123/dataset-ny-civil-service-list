import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {};
  componentDidMount = () =>
    fetch('/api/time')
      .then(res => res.json())
      .then(data => {this.setState({time:data.time})})

  render() {
    const state = this.state;
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <p>The current time is {state.time}</p>
      </div>
    );
  }
}

export default App;
