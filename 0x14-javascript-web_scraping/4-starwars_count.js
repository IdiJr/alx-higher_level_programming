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
    let charList = [];
    for (const film of JSON.parse(body).results) {
      charList = charList.concat(film.characters);
    }
    const wedgeAntilles = charList.filter(x => x.includes(`/${characterId}/`));
    console.log(wedgeAntilles.length);
  }
});
