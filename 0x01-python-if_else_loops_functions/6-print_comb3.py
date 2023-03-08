#!/usr/bin/python3
for k in range(0, 10):
    for c in range(k + 1, 10):
        if k == 8 and c == 9:
            print("{}{}".format(k,c))
        else:
            print("{}{}".format(k, c), end=", ")
