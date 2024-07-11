import React, { useState, useEffect } from 'react';
import './App.css'; // Assuming you have a CSS file for styling

const Shop = () => {
  const [drinks, setDrinks] = useState([]);

  useEffect(() => {
    fetchDrinks();
  }, []);

  const fetchDrinks = async () => {
    try {
      const response = await fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita');
      const data = await response.json();
      setDrinks(data.drinks); // Assuming 'drinks' is the array of drinks in your JSON
    } catch (error) {
      console.error('Error fetching drinks:', error);
    }
  };

  return (
    <div className="app">
      <h1 className="title">Popular Margarita Cocktails</h1>
      <div className="drinks-container">
        {drinks.map(drink => (
          <div key={drink.idDrink} className="drink-card">
            <img className="drink-img" src={drink.strDrinkThumb} alt={drink.strDrink} />
            <div className="drink-details">
              <h2 className="drink-name">{drink.strDrink}</h2>
              <p className="drink-instructions">{drink.strInstructions}</p>
              <p className="drink-ingredients">
                <strong>Ingredients:</strong> {drink.strIngredient1}, {drink.strIngredient2}, {drink.strIngredient3}
              </p>
            </div>
          </div>
        ))}
      </div>
      </div>
  );
};

export default Shop;