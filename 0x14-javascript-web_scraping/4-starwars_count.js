#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
const searchUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
req.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    let count = 0;
    for (const film of data.results) {
      if (film.characters.includes(searchUrl)) {
        count++;
      }
    }
    console.log(count);
  }
});
