#!/usr/bin/node

exports.converter = function (base) {
  return convert => convert.toString(base);
};
