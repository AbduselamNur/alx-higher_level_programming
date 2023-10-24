#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
let count = 0;
req(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
