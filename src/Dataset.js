import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Info} from './Info.js';


class Dataset extends Component {
  state = {};
  componentDidMount = () =>
    fetch(`/api/${this.props.match.params.dataset}`)
      .then(res => res.json())
      .then(data => {
        let { total, columns } = data
        this.setState({count:total, columns})
      })

  render() {
    const state = this.state;
    const columns = this.state.columns;
    let params = this.props.match.params || null;
    let info = <Info columns={columns}/>;
    console.log(this.state)
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <p>Current dataset is {params.dataset}</p>
        <p>Dataset count {state.count}</p>
        {info}
      </div>
    );
  }
}

export default Dataset;