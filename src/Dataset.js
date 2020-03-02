import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

// export const Dataset = () =>
//   <Router>
//     <Switch>
//       <Route path="/" exact={true} component={Home} />
//       {/* <Route path="/:dataset" component={Dataset} /> */}
//     </Switch>
//   </Router>

class Dataset extends Component {
  state = {};
  componentDidMount = () =>
    fetch(`/api/${this.props.match.params.dataset}`)
      .then(res => res.json())
      .then(data => {this.setState({count:data.total})})

  render() {
    const state = this.state;
    let params = this.props.match.params || null;

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
      </div>
    );
  }
}

export default Dataset;