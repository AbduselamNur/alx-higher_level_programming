#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv)
    print("{} ".format(args - 1), end="")
    if leng == 1:
        print("arguments.")
    elif leng > 1:
        if leng == 2:
            print("argument:")
        elif leng > 2:
            print("arguments:")
        for i in range(args - 1):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
