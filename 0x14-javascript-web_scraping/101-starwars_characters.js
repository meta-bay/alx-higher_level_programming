#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, async (err, response, body) => {
  if (err) { console.error(err); }
  const result = JSON.parse(body);
  const characters = result.characters;
  for (const charLink of characters) {
    await new Promise((resolve, reject) => {
      request(charLink, (e, r, body) => {
        if (e) { reject(e); }
        const theChar = JSON.parse(body);
        console.log(theChar.name);
        resolve();
      });
    });
  }
});
