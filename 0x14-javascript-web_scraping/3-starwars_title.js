#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = url + process.argv[2];
req(movieId, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
