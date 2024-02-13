#!/usr/bin/node
const theDict = require('./101-data').dict;

const newDict = {};

for (const [key, value] of Object.entries(theDict)) {
  newDict[value] ? newDict[value].push(key) : (newDict[value] = [key]);
}

console.log(newDict);
