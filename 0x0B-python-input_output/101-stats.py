#!/usr/bin/python3
import sys


def p_info():
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

c = 0
file_size = 0

try:
    for line in sys.stdin:
        if c != 0 and c % 10 == 0:
            p_info()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except:
            pass

        try:
            file_size += int(pieces[-1])
        except:
            pass

        c += 1

    p_info()
except KeyboardInterrupt:
    p_info()
    raise
