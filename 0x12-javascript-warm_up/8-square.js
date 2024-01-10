#!/usr/bin/node

let arg = process.argv[2];

arg = parseInt(arg, 10);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let k = 0; k < arg; k++) {
    let row = '';
    for (let j = 0; j < arg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
