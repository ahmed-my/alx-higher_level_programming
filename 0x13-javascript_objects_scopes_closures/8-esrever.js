#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = list.slice();
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    const tmp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = tmp;
  }

  return reversedList;
};
