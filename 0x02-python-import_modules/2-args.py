#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lengt = len(sys.argv)
    print("{} ".format(lengt - 1), end="")
    if lengt == 1:
        print("arguments.")
    elif lengt > 1:
        print("argument:")
    for x in range(2, lengt + 1):
        print("{}: {}".format(x, sys.argv[x - 1]))
