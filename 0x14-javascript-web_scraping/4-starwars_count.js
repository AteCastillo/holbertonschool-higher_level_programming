#!/usr/bin/node
const request = require('request');
const api = process.argv[2].slice(0, -5) + "/people/18"

request(api, function(err, response, body) {
  let array = JSON.parse(body).films
  console.log(array.length)
});




