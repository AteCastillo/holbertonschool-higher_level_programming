#!/usr/bin/node

if (process.argv[2] == null) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  process.argv.sort((a, b) => a - b);
  console.log(process.argv[process.argv.length - 2]);
}
