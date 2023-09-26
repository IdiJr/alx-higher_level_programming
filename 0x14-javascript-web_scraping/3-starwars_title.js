#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${episode}`;
request(link, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
