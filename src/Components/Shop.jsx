import React from 'react';
import './Shop.css'; // Ensure to create this CSS file

function Shop() {
  const items = [
    {
      id: 1,
      image: 'https://via.placeholder.com/300',
      price: '$20.00',
      description: 'This is a great product.',
      quantity: '5 available',
    },
    {
      id: 2,
      image: 'https://via.placeholder.com/300',
      price: '$15.00',
      description: 'This product is amazing.',
      quantity: '2 available',
    },
    // Add more items here
  ];

  return (
    <div className="shop-container">
      {items.map(item => (
        <div className="card" key={item.id}>
          <img className="card-image" src={item.image} alt={item.description} />
          <div className="card-content">
            <p className="card-price">{item.price}</p>
            <p className="card-description">{item.description}</p>
            <p className="card-quantity">{item.quantity}</p>
            <button className="card-button">Add to Cart</button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Shop;
