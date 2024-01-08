#!/usr/bin/node
const x = process.argv[2];
const intFirst = parseInt(x, 10);
if (!isNaN(intFirst)) {
  for (let i = 0; i < intFirst; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
