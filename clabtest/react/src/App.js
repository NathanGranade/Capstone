import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import React, { useState } from 'react';
import Home from './component/home';
import Contact from './component/contact';
import Drop from './component/drop';
import Register from './component/register';
import Login from './component/login';
import SavedTabs from './component/savedtabs';

import './App.css';

const [showAlternate, setShowAlternate] = useState(false);
  
function Navbar() {
  const location = useLocation();
  const isDropOrRegisterRoute = location.pathname === '/drop' || location.pathname === '/register';
  $.ajax({
    url: '/loggedin',
    success: function(data) {
        console.log(data.variable);
    }

});
  showAlternate = data;
  if (showAlternate){
  return (
    <ul className="nav-list">
      <li><a href="/">Home</a></li>
      {!isDropOrRegisterRoute && <li><a href="#about">About</a></li>}
      {!isDropOrRegisterRoute && <li><a href="#contact">Contact</a></li>}
      <li><a href="register" id="register">Sign Up</a></li>
      <li><a href="savedtabs" id="savedtabs">Saved Tabs</a></li>
    </ul>
  );
}
else
return (
  <ul className="nav-list">
    <li><a href="/">Home</a></li>
    {!isDropOrRegisterRoute && <li><a href="#about">About</a></li>}
    {!isDropOrRegisterRoute && <li><a href="#contact">Contact</a></li>}
    <li><a href="register" id="register">Sign Up</a></li> 
    <li><a href="savedtabs" id="savedtabs">Saved Tabs</a></li>
  </ul>
);
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
