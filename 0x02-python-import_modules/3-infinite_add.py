#!/usr/bin/python3
if __name__ == "__main__":
    import sys

total = 0
number = len(sys.argv) - 1

for k in range(number):
    total = total + int(sys.argv[k+1])
print("{}".format(total))
