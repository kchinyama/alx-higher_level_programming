#!/usr/bin/node

module.exports = class Rectangle {
	constructor(w, h) {
		if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
			this.width = w;
			this.height = h;
		} else {
			return undefined;
		}
	}
	print() {
		for (let k = 0; k < this.height; k++) {
			console.log('X'.repeat(this.width));
		}
	}

	rotate() {
		[this.width, this.height] = [this.height, this.width];
	}

	double() {
		this.width *= 2;
		this.height *=2;
		
	}
};

