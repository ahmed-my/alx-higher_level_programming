#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const contentToWrite = process.argv[3];
if (!filePath || !contenToWrite) {
  console.error('provide first and second argument from command line');
}
fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
