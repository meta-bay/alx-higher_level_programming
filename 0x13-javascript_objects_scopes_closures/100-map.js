#!/usr/bin/node

const theList = require('./100-data').list;
console.log(theList);
const newList = theList.map((curr, idx) => curr * idx);
console.log(newList);
