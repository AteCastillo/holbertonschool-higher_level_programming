#!/usr/bin/node
exports.converter = function (base) {
  return number => number.toString(base);
  // it is the same as:
  // funtion name (number, base){
  //    return number.toString(base);
  // }
};
