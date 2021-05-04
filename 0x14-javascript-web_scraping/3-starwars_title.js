#!/usr/bin/node
const request = require('request');
const episode_api = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];

request(episode_api, function (err, response, body) {
  console.log(JSON.parse(body).title);
});
