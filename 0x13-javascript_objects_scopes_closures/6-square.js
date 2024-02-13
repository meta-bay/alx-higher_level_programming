#!/usr/bin/node

const theParent = require('./5-square');

module.exports = class Square extends theParent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let h = 0; h < this.height; h++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
