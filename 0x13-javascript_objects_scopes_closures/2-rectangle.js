#!/usr/bin/node
module.exports = class Rectanle {
  constructor (width, height) {
    if (Number.isInteger(width) && Number.isInteger(height) && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
};
