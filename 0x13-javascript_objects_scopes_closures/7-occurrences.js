#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurs = 0;
  for (const i of list) {
    if (i === searchElement) occurs++;
  }
  return occurs;
};
