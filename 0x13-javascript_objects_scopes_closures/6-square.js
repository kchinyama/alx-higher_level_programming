#!/usr/bin/node
class Rectangle {
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
}

class Square extends Rectangle {
	constructor(size) {
		super(size, size);
	}
}

module.exports class Square extends Square {
	charPrint(c) {
		if (c === undefined) c = 'X';
		for (let k = 0; k < this.height; k++) {
                        console.log('c'.repeat(this.width));
		}
	}
}
