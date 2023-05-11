#!/usr/bin/node

const args = process.argv.slice(2);
if (!args[0] || isNaN(args[0])) {
  console.log('Missing size');
}
for (let i = 0; i < args[0]; i++) {
  let row = '';
  for (let j = 0; j < args[0]; j++) {
    row = row + 'X';
  }
  console.log(row);
}
