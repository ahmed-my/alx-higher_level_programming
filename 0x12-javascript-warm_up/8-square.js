#!/usr/bin/node
const size = process.argv[2];
const sizeInt = parseInt(size, 10);
if (!isNaN(sizeInt)) {
  for (let i = 0; i < sizeInt; i++) {
    let row = '';
    for (let j = 0; j < sizeInt; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
