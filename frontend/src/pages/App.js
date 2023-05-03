import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import Home from '../components/home';
import Contact from '../components/contact';
import Drop from '../components/drop';
import Register from '../components/register';
import Login from '../components/login';
import SavedTabs from '../components/savedtabs';

import '../css/app.css';

function Navbar() {
  const location = useLocation();
  const isDropOrRegisterRoute = location.pathname === '/drop' || location.pathname === '/register';
  const loggedin = false
  if (loggedin === false){
  return (
    <ul className="nav-list">
      <li><a href="/">Home</a></li>
      {!isDropOrRegisterRoute && <li><a href="#about">About</a></li>}
      {!isDropOrRegisterRoute && <li><a href="#contact">Contact</a></li>}
      <li><a href="register" id="register">Sign Up</a></li>
    </ul>
  );
  }
  if (loggedin === true){
    return (
      <ul className="nav-list">
        <li><a href="/">Home</a></li>
        {!isDropOrRegisterRoute && <li><a href="#about">About</a></li>}
        {!isDropOrRegisterRoute && <li><a href="#contact">Contact</a></li>}
        <li><a href="savedtabs" id="savedtabs">Saved Tabs</a></li>
      </ul>
    );
    }
}


class App extends Component {
  render() {
    return (
      <Router>
        <div className="navbar">
          <Navbar />
          <Routes>
            <Route exact path="/" element={<Home />}></Route>
            <Route exact path="/contact" element={<Contact />}></Route>
            <Route exact path="/drop" element={<Drop />}></Route>
            <Route exact path="/register" element={<Register />}></Route>
            <Route exact path="/login" element={<Login />}></Route>
            <Route exact path="/savedtabs" element={<SavedTabs />}></Route>
          </Routes>
        </div>
      </Router>
    );
  }
}

export default App;
