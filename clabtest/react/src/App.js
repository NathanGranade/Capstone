import React, { Component } from 'react';
import { BrowserRouter as Router,Routes, Route} from 'react-router-dom';
import Home from './component/home';
import Contact from './component/contact';
import Drop from './component/drop';
import Register from './component/register';



import './App.css';
  
class App extends Component {
  render() {
    return (
       <Router>
        <div className="navbar" >
            <ul className="nav-list">
                <li><a href="/">home</a></li>
                <li><a href="#about">about</a></li>
                <li><a href="#contact">contact</a></li>
                <li><a href="register" id="register">sign up</a></li>
            </ul>
			    <Routes>
                <Route exact path='/' element={< Home />}></Route>
                <Route exact path='/contact' element={< Contact />}></Route>
                <Route exact path='/drop' element={< Drop />}></Route>
			          <Route exact path='/register' element={< Register />}></Route>
                
          </Routes>
        </div>
       </Router>
   );
  }
}
export default App;