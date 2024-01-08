#!/usr/bin/node
const arg = process.argv[2];
const intValue = parseInt(arg, 10);
if (!isNaN(intValue)) {
  console.log('My number: ' + intValue);
} else {
  console.log('Not a number');
}
