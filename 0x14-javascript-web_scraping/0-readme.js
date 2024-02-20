#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
if (!filepath) {
  process.exit(1);
}
fs.readFile(filepath, 'utf8', (err, content) => {
  if (err) {
    console.error(err);
  } else {
    console.log(content);
  }
});
