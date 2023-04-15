#!/usr/bin/node

const fs = require('fs');
function concatFiles (srcFile1, srcFile2, destFile) {
  const data1 = fs.readFileSync(srcFile1);
  const data2 = fs.readFileSync(srcFile2);
  const data = data1 + data2;
  fs.writeFileSync(destFile, data);
}

const args = process.argv.slice(2);
if (args.length !== 3) {
  console.error('Usage: concat.js <srcFile1> <srcFile2> <destFile>');
  process.exit(1);
}

const srcFile1 = args[0];
const srcFile2 = args[1];
const destFile = args[2];

concatFiles(srcFile1, srcFile2, destFile);
