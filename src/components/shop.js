import React, { useState, useEffect } from 'react';
import './App.css'; // Assuming you have a CSS file for styling
import SearchBar from './SearchBar'; // Import the SearchBar component

const Shop = () => {
  const [drinks, setDrinks] = useState([]);
  const [filteredDrinks, setFilteredDrinks] = useState([]);

  useEffect(() => {
    fetchDrinks();
  }, []);

  const fetchDrinks = async () => {
    try {
      const response = await fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita');
      const data = await response.json();
      setDrinks(data.drinks); // Assuming 'drinks' is the array of drinks in your JSON
      setFilteredDrinks(data.drinks); // Initialize filteredDrinks with all drinks
    } catch (error) {
      console.error('Error fetching drinks:', error);
    }
  };

  const handleSearch = (query) => {
    // Perform filtering based on the search query
    const filtered = drinks.filter(drink =>
      drink.strDrink.toLowerCase().includes(query.toLowerCase())
    );
    setFilteredDrinks(filtered);
  };

  return (
    <div className="app">
      <h1 className="title">Popular Margarita Cocktails</h1>
      <SearchBar placeholder="Search cocktails..." data={drinks} onSearch={handleSearch} />
      <div className="drinks-container">
        {filteredDrinks.map(drink => (
          <div key={drink.idDrink} className="drink-card">
            <img className="drink-img" src={drink.strDrinkThumb} alt={drink.strDrink} />
            <div className="drink-details">
              <h2 className="drink-name">{drink.strDrink}</h2>
              <p className="drink-instructions">{drink.strInstructions}</p>
              <p className="drink-ingredients">
                <strong>Ingredients:</strong> {drink.strIngredient1}, {drink.strIngredient2}, {drink.strIngredient3}
                <br />
                <button onClick={() => addToCart(drink)}>ADD TO CART</button>
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Shop;
