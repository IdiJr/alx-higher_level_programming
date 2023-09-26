#!/usr/bin/node
const request = require('request');
const link = process.argv[2];
const characterId = 18;
request(link, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    const wedgeAntilles = JSON.parse(body).results.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(wedgeAntilles.length);
  }
});
