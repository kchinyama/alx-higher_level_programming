#!/usr/bin/node

function printSquare(k) {
  const numX = parseInt(k);

  if (isNaN(numX)) {
    console.log('Missing size');
  }

  for (let i = 0; i < numX; i++) {
    console.log('X');
	  for (let k = 0; k < numX; k++)
		  console.log('X');
  }
}

const arg = process.argv[2];
printSquare(arg);

