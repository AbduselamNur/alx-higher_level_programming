#!/usr/bin/node
module.exports = class Rectanle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    } else {
      return 0;
    }
  }
};
