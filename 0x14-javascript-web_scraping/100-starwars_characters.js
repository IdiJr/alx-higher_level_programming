#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(link, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movieCharacters = JSON.parse(body).characters;
  movieCharacters.forEach((movieCharacters) => {
    request(movieCharacters, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }
      if (charResponse.statusCode === 200) {
        console.log(JSON.parse(charBody).name);
      } else {
        console.error(`Failed to fetch character data. Status code: ${charResponse.statusCode}`);
      }
    });
  });
});
