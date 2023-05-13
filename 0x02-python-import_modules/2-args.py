#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lengt = len(sys.argv)
    print("{} arguments.".format(lengt - 1))
    for x in range(2, lengt + 1):
        print("{}: {}".format(x, sys.argv[x - 1]))
