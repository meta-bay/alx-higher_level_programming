#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (err, response, body) => {
  if (err) { console.error(err); }
  const result = JSON.parse(body);
  const characters = result.characters;
  characters.forEach(charUrl => {
    request(charUrl, (e, r, body) => {
      if (e) { console.error(e); }
      const char = JSON.parse(body);
      console.log(char.name);
    });
  });
});
