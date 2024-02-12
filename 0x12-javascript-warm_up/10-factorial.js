#!/usr/bin/node

function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }
  return (num * factorial(num - 1));
}
const num = Number(process.argv[2]);
const the_factorial = factorial(num);
console.log(the_factorial);
