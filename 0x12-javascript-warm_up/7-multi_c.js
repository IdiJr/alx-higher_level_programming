#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  let x = parseInt(process.argv[2]);
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
}
