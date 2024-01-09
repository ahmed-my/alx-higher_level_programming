#!/usr/bin/node
function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));

/*
const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
};
const arg = parseInt(process.argv[2], 10);
console.log(factorial(arg));

const factorial = function fac(n) {
  return n < 2 ? 1 : n * fac(n - 1);
};

const arg = parseInt(process.argv[2], 10);
if (!isNaN(arg)) {
  const result = factorial(arg);
  console.log(result);
} else {
  console.log(1);
}
*/
