#!/usr/bin/node
const dict = require('./101-data').dict;

const listSort = Object.entries(dict);
const value = Object.values(dict);
const uniqueValue = [...new Set(value)];
const dictNew = {};
for (const j in uniqueValue) {
  const list = [];
  for (const k in listSort) {
    if (listSort[k][1] === uniqueValue[j]) {
      list.unshift(listSort[k][0]);
    }
  }
  dictNew[uniqueValue[j]] = list;
}
console.log(dictNew);
