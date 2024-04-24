#!/usr/bin/node

function printSquare(k) {
  const numX = parseInt(k);

  if (isNaN(numX)) {
    console.log('Missing size');
  }

  for (let i = 0; i < numX; i++) {
	  console.log('X'.repeat(numX));
}

const arg = process.argv[2];
printSquare(arg);

