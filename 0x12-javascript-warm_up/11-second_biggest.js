#!/usr/bin/node

if (process.argv.length < 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2);
  const num = numbers.map(Number);

  let biggest = num[0];
  for (let i = 0; i < num.length; i++) {
    biggest = (biggest > num[i]) ? biggest : num[i];
  }
  let secondBig = 0;
  for (let j = 0; j < num.length; j++) {
    secondBig = (num[j] > secondBig && num[j] < biggest) ? num[j] : secondBig;
  }
  console.log(secondBig);
}
