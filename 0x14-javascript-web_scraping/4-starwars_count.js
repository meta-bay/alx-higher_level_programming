#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let waCount = 0;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const movies = JSON.parse(body).results;
  for (let i = 0; i < movies.length; i++) {
    for (let j = 0; j < movies[i].characters.length; j++) {
      if (movies[i].characters[j].includes(18)) {
        waCount += 1;
      }
    }
  }
  console.log(waCount);
});
