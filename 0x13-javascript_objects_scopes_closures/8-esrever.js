#!/usr/bin/node

exports.esrever = function (list) {
	let newList = [];

	for (let k = list.length; k > 0; k--) {
		newList.push(list.pop());
	}
	return newList;
}
