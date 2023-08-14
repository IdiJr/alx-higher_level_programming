#!/usr/bin/node

const numArguments = process.argv.length;
if (numArguments === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
