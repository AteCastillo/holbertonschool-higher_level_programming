#!/usr/bin/node
const request = require('request');
const episodeapi = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(episodeapi, function (response, body) {
  console.log(JSON.parse(body).title);
});
