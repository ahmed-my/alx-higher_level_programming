#!/usr/bin/node
const request = require('request');
const APIURL = process.argv[2];
request(APIURL, (err, response, body) => {
  if (!err) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
