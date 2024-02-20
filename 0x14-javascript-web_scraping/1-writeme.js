#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const content_to_write = process.argv[3];
fs.writeFile(filePath, content_to_write, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
