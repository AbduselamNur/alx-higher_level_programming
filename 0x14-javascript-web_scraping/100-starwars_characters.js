#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

request.get(`https://swapi.dev/api/films/${movieId}`, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    let count = 0;
    const printCharacterName = () => {
      if (count === characters.length) {
        return;
      }
      const characterUrl = characters[count];
      request.get(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          const characterData = JSON.parse(body);
          const characterName = characterData.name;
          console.log(characterName);
          count++;
          printCharacterName();
        }
      });
    };
    printCharacterName();
  }
});
