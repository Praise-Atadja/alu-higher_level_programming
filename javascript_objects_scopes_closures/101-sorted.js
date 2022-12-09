#!/usr/bin/node
const dict = require('./101-data.js').dict;
let firstdict = {};
for (let key in dict) {
  if (firstdict[dict[key]] === undefined) {
    firstdict[dict[key]] = [key];
  } else {
    firstdict[dict[key]].push(key);
  }
}
console.log(firstdict);
