#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_number = len(argv)
    index = 1

    if argv_number == 0:
        print("{:d} arguments.".format(argv_number))
    elif argv_number == 1:
        print("{:d} argument:".format(argv_number))
        print("{:d}: {:s}".format(index, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_number))
        while index <= argv_number:
            print("{:d}: {:s}".format(index, sys.argv[index]))
            index = index + 1
