#!/usr/bin/node

const argv = process.argv.slice(2);

let len = 0;

for (const arg in argv) {
  len++;
}
if (len === 0) {
  console.log('No argument');
} else if (len === 1) {
  console.log(`${argv[0]}`);
}
