#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (error, content) {
  if (error) throw error;
  console.log(content);
});
