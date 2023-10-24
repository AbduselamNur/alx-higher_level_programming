#!/usr/bin/node

const url = process.argv[2];
const req = require('request');

req.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const results = {};
    const data = JSON.parse(body);
    for (const task of data) {
      const userId = task.userId;
      const done = task.completed;
      if (done) {
        if (results[userId]) {
          results[userId]++;
        } else {
          results[userId] = 1;
        }
      }
    }
    console.log(results);
  }
});
