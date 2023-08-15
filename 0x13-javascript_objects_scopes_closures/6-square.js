#!/usr/bin/node
const mainSquare = require('./5-square');

class Square extends mainSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; ++i) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
