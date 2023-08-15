#!/usr/bin/Node
exports.converter = function (base) {
  return number => number.toString(base);
};
