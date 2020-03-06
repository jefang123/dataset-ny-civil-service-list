import React from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from './Home.js' 
import Dataset from './Dataset.js'

export const App = () =>
  <Router>
    <Switch>
      <Route path="/" exact={true} component={Home} />
      {/* <Route path="/:state" component={Home} /> */}
      <Route path="/:state/:dataset" component={Dataset} />
    </Switch>
  </Router>


