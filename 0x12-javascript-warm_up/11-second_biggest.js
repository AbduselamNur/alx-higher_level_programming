#!/usr/bin/node

function secBig (args) {
  if (!isNaN(args) || args.length === 1) {
    return 0;
  }
  args.sort((a, b) => b - a);
  return args[1];
}
const arg = process.argv.slice(2).map(Number);
console.log(secBig(arg));
