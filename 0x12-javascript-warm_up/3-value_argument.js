#!/usr/bin/node

const { argv } = require('process');
if (argv[2] === undefined ) {
  console.log('No argument');
}

let i = 2;
while (argv[i]) {
  console.log(argv[i]);
  i++;
}
