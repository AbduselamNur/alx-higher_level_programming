#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ar = len(sys.argv)
    print("{} ".format(ar - 1), end="")
    if ar == 1:
        print("arguments.")
    elif ar > 1:
        if ar == 2:
            print("argument:")
        elif ar > 2:
            print("arguments:")
        for i in range(ar - 1):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
