#!/usr/bin/python3
import sys


def print_info():
    print('File size: {:d}'.format(file_size))

    for s, c in sorted(s.items()):
        if c > 0:
            print('{}: {:d}'.format(s, c))


s = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

lc = 0
file_size = 0

try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_info()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in s.keys():
                s[str(status)] += 1
        except:
            pass

        try:
            file_size += int(pieces[-1])
        except:
            pass

        lc += 1

    print_info()
except KeyboardInterrupt:
    print_info()
    raise
