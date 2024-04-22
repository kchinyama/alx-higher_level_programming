#!/usr/bin/node

function printCIsFun(k) {
  const numOccurrences = parseInt(k);

  if (isNaN(numOccurrences)) {
    console.log('Missing number of occurrences');
  }

  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}

const arg = process.argv[2];
printCIsFun(arg);

