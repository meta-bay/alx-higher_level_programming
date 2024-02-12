#!/usr/bin/node

const { argv } = require('node:process');
if (argv[2] == null) {
  console.log('No argument');
}

let i = 2;
while (argv[i]) {
  console.log(argv[i]);
  i++;
}
