#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    count = 0

    for k in range(0, x):
        try:
            print("{}".format(my_list[k]), end="")
            count = count + 1
        except:
            pass
    print()
    return count
