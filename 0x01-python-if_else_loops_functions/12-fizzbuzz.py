#!/usr/bin/python3
def fizzbuzz():
    for k in range(101):
        if k % 3 == 0:
            print("Fizz", end="")
        if k % 5 == 0:
            print("Buzz", end="")
        if (k % 3 == 0) and (k % 5 == 0):
            print("Fizz Buzz", end="")
        else:
            print("{}".format(k, end=""))
