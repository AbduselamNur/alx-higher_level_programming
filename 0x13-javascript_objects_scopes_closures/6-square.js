#!/usr/bin/node

const S = require('./5-square');
module.exports = class Square extends S {
  constructor (size) {
    super(size, size);
  }
  charPrint (c = 'X') {
   super.print(c)
  }
};
