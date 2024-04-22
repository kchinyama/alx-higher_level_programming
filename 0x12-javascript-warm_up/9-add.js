#!/usr/bin/node

function add(a, b) {
  const sum = a + b;
  console.log(sum);
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (isNaN(arg1) || isNaN(arg2)) {
  return;
} else {
  add(arg1, arg2);
}

