#!/usr/bin/node

exports.callMeMoby = function repeat (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
