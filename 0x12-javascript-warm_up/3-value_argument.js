#!/usr/bin/node

const { argv } = require('process');
if (argv[2] === undefined ) {
  console.log('No argument');
}
console.log(argv[2]);
