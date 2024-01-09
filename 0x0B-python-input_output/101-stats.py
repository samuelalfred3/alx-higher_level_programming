#!/usr/bin/python3
"""
Module for computing metrics from stdin
"""

import sys

def print_metrics(status_codes, file_size):
    """
    Prints the metrics
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    try:
        for i, line in enumerate(sys.stdin, 1):
            data = line.split()
            if len(data) > 2:
                status_code = data[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                file_size += int(data[-1])
            if i % 10 == 0:
                print_metrics(status_codes, file_size)
    except KeyboardInterrupt:
        print_metrics(status_codes, file_size)
        raise
    print_metrics(status_codes, file_size)
