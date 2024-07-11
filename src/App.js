import Login from './components/Login';
import './App.css';
import Shop from './components/Shop';
import { BrowserRouter,Route,Link,Routes,NavLink } from "react-router-dom";
import Register from './components/Register';

function App() {
  return (
    <BrowserRouter>
    <header>
      <nav>
        <h1>cross</h1>
        <div id='links'>
        <NavLink to={"/"}>login</NavLink>
        <NavLink to={"/shop"}>Shop</NavLink>
        <NavLink to={"/register"}>Sign up</NavLink>
        </div>
      </nav>
    </header>
    <div>
      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route path="/shop" element={<Shop/>}/>
        <Route path="/register" element={<Register/>}/>
      </Routes> 
    </div>
    </BrowserRouter>
  )
}

export default App;
