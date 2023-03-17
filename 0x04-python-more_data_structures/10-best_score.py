#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = 0
    for k, value in a_dictionary.items():
        if value > biggest:
            biggest = value
    for k, value in a_dictionary.items():
        if value == biggest:
            return k
