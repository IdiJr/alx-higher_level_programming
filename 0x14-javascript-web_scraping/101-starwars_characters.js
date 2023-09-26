#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(link, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    const movieCharacters = JSON.parse(body).characters;
    function fetchCharacter (index) {
      if (index === movieCharacters.length) {
        return;
      }
      request(movieCharacters[index], (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else if (charResponse.statusCode === 200) {
          console.log(JSON.parse(charBody).name);
        } else {
          console.error(`Failed to fetch character data. Status code: ${charResponse.statusCode}`);
        }
        fetchCharacter(index + 1);
      });
    }
    fetchCharacter(0);
  } else {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
  }
});
