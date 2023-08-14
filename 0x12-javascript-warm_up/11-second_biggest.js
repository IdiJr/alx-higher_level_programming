#!/usr/bin/node

function secondLargest (a, b) {
  return (b - a);
}

if (process.argv[2] === undefined || process.argv.lenth < 4) {
  console.log('0');
} else if (process.argv.length <= 3) {
  console.log('0');
} else {
  const size = process.argv.length;
  const numbers = [];
  for (let i = 2; i < size; i++) {
    numbers.push(parseInt(process.argv[i]));
  }
  numbers.sort(secondLargest);
  console.log(numbers[1]);
}
