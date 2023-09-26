#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const link = process.argv[2];
const filePath = process.argv[3];
request(link, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      }
    });
  } else {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  }
});
