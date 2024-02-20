#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, (error, response, body) => {
  console.log(error || JSON.parse(body).title);
});
