#!/usr/bin/node
let square = '';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      square += 'X';
    }
    if (i < parseInt((process.argv[2] - 1))) {
      square += '\n';
    }
  }
  console.log(square);
}
