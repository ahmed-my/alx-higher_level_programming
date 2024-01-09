#!/usr/bin/node
const SquareOf = require('./5-square');

class Square extends SquareOf {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
