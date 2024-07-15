import React, { useEffect, useState } from 'react';

const Shop = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch('/home/joey/development/code/shopping-mall/products.json'); // Replace with your endpoint or file path
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
          // throw new TypeError('Expected JSON response from server');
        }
        const data = await response.json();
        setProducts(data.products);
      } catch (error) {
        // console.error('Error fetching data:', error);
        // Handle error state or retry logic here
      }
    };
  
    fetchProducts();
  }, []);

  return (
    <div>
      <h2>Products</h2>
      <div className="product-list">
        {products.map(product => (
          <div key={product.id} className="product">
            <img src={product.image_url} alt={product.name} />
            <div>
              <h3>{product.name}</h3>
              <p>{product.description}</p>
              <p>Price: ${product.price}</p>
              <p>Stock: {product.stock_quantity}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Shop;