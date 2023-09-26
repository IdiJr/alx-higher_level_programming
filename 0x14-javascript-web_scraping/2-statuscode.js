#!/usr/bin/node
const request = require('request');
const link = process.argv[2];
request(link, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
