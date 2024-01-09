#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let s = 0; s < list.length; s++) {
    if (searchElement === list[s]) {
      count += 1;
    }
  }
  return count;
};
