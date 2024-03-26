#!/usr/bin/node

const request = require('request');
const filmId = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(filmId, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
