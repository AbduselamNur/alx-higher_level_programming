#!/usr/bin/node
module.exports = class Rectanle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return 0;
    }
  }
};
