#!/usr/bin/node

let arg = process.argv[2];

arg = parseInt(arg, 10);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let k = 0; k < arg; k++) {
    console.log('C is fun');
  }
}
