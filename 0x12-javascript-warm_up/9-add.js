#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  a = Number(args[0]);
  b = Number(args[1]);

  if (!args[0] || !args[1]) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(args[0], args[1]);
