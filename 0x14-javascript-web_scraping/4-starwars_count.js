#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
const searchUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
req(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const count = data.results.filter((film) => {
      return film.characters.includes(searchUrl);
    }).length;
    console.log(count);
  }
});
