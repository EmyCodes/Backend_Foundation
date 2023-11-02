#!/usr/bin/node

const myNum = [1, -1, 2, -2, 3, -3, 4, -100, 5];

const myFilter = removeNNeg(myNum, (x) => x >= 0);

function removeNNeg(myNum, callback) {
  const myArray = [];
  for (const x of myNum) {
    if (callback(x)) {
      myArray.push(x);
    }
  }
  return myArray;
}
console.log(myFilter);