#!/usr/bin/python3
def fizzbuzz():
    for k in range(101):
        print(k, end=" ")
        if k % 3 == 0:
            print("Fizz")
        if k % 5 == 0:
            print("Buzz")
        if (k % 3 == 0) and (k % 5 == 0):
            print("Fizz Buzz")
