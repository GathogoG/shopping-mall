

import Home from './components/Home';
import './App.css';
import ShoppingCart from './components/ShoppingCart';
import { BrowserRouter,Route,Routes,NavLink } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
    <header>
      <nav>
        <h1>Welcome To My Shopping Mall</h1>
        <div id = 'Link'>
        <NavLink to={"/"}>Home</NavLink>
        <NavLink to={"/ShoppingCart"}>ShoppingCart</NavLink>
        
        </div>
      </nav>
    </header>
    <div>
      <Routes>
        <Route path="/Home" element={<Home/>}/>
        <Route path="/ShoppingCart" element={<ShoppingCart/>}/>
      </Routes> 
    </div>
    </BrowserRouter>
  )
}

export default App;