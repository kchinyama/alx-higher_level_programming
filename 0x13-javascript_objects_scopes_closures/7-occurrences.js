#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	let counter = 0;

	for (num of list.flat()) {
		if (num === searchElement) {
			counter++;
		}
	};
	return counter;
}
