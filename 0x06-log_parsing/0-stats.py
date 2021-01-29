#!/usr/bin/python3
"""
    This script reads stdin line by line and computes metrics
"""
import sys


def print_stats(filesize, codeKey):
    """ Method to Print Stats about Status code """
    print("File size: {:d}".format(filesize))
    for key in sorted(codeKey.keys()):
        if codeKey[key] != 0:
            print("{}: {:d}".format(key, codeKey[key]))

if __name__ == "__main__":
    filesize = 0
    countLine = 0
    codeKey = {
        '200': 0, '301': 0, '400': 0,
        '401': 0, '403': 0, '404': 0,
        '405': 0, '500': 0
    }

    try:
        for line in sys.stdin:
            line = line.split()

            if len(line) >= 2:

                if line[-2] in codeKey.keys():
                    codeKey[line[-2]] += 1

                filesize += int(line[-1])
                countLine += 1

                if not countLine % 10:
                    print_stats(filesize, codeKey)
        print_stats(filesize, codeKey)
    except KeyboardInterrupt:
        print_stats(filesize, codeKey)
        raise
