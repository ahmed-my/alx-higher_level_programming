#!/usr/bin/node
const add = function (a, b) {
  return a + b;
};
const x = parseInt(process.argv[2], 10);
const y = parseInt(process.argv[3], 10);
console.log(add(x, y));
