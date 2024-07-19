import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './Shop.css';  // Assuming you have a CSS file for styling

function Shop() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetch('https://shopping-backend-wlu9.onrender.com/products')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        if (data && Array.isArray(data.products)) {
          setItems(data.products);
        } else {
          setError('Data is not in the expected format');
        }
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching items:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  const handleAddToCart = (item) => {
    // Decrease stock quantity
    const updatedItem = { ...item, stock_quantity: item.stock_quantity - 1 };

    // Update the backend stock quantity and add to cart
    fetch(`https://shopping-backend-wlu9.onrender.com/cart/add`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ product_id: item.id, quantity: 1 })
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to add item to cart');
        }
        return response.json();
      })
      .then(() => {
        // Update state with the new stock quantity
        setItems(items.map(i => (i.id === item.id ? updatedItem : i)));

        // Navigate to the cart page
        navigate('/cart');
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="shop-container">
      {items.map(item => (
        <div key={item.id} className="card">
          <img src={item.image_url} alt={item.description} className="card-image"/>
          <div className="card-content">
            <h3 className="card-title">{item.name}</h3>
            <p className="card-price">${item.price.toFixed(2)}</p>
            <p className="card-description">{item.description}</p>
            <p className="card-stock">Stock: {item.stock_quantity}</p>
            <button 
              className="card-button" 
              onClick={() => handleAddToCart(item)} 
              disabled={item.stock_quantity === 0}
            >
              {item.stock_quantity === 0 ? 'Out of Stock' : 'Add to Cart'}
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Shop;
