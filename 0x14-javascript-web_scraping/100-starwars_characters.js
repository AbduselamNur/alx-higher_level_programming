#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

req(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    req(characters[i], (err, response, body) => {
      if (err) {
        console.error(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
