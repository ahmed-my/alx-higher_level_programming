#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const contentToWrite = process.argv[3];
if (!filePath || !contentToWrite) {
  process.exit(1);
}
fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
