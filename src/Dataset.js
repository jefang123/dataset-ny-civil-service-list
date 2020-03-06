import React, { Component } from 'react';
import logo from './logo.svg';
import {Info} from './Info.js';


class Dataset extends Component {
  state = {};
  componentDidMount = () =>
    fetch(`/info/${this.props.match.params.dataset}`)
      .then(res => res.json())
      .then(data => {
        let { dataset_name, total, columns } = data
        this.setState({dataset_name, count:total, columns})
      })
  
  // onSubmit = () => 
  //   fetch(`/api/${this.props.match.params.dataset}`)
  //   .then(res => res.json())
  //   .then(data => {
  //     let { dataset_name, total, columns } = data
  //     this.setState({dataset_name, count:total, columns})
  //   })

  render() {
    const { dataset_name, count, columns } = this.state;
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
        <p>Current dataset is {dataset_name}</p>
        <p>Dataset count {count}</p>
        {info}
      </div>
    );
  }
}

export default Dataset;