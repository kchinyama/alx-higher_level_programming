#!/usr/bin/node

const k = process.argv[2];

if (process.argv.length === 2) {
  console.log('Not a number');
} else if (isNaN(k)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + k);
}
