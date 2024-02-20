#!/usr/bin/node
const request = require('request');
const movie_id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;
request(url, (error, response, body) => {
  console.log(error || JSON.parse(body).title);
});
