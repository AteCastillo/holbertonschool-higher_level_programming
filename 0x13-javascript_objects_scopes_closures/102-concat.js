#!/usr/bin/node
const fs = require('fs');

const new1 = fs.readFileSync(process.argv[2], { encoding: 'utf8', flag: 'r' });
const new2 = fs.readFileSync(process.argv[3], { encoding: 'utf8', flag: 'r' });

fs.writeFileSync(process.argv[4], new1 + new2);
