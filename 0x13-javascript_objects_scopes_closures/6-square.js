#!/usr/bin/node
const Parent = require('./5-square');
class Square extends Parent {
  charPrint (c) {
    let rectangle = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rectangle += c !== undefined ? c : 'X';
      }
      if (i < this.height - 1) {
        rectangle += '\n';
      }
    }
    console.log(rectangle);
  }
}
module.exports = Square;
