#!/usr/bin/python3
'''
    Log parsing
'''


def print_stats(size, stat_code):
    '''
        reads stdin line by line
    '''
    print("File size: {}".format(size))
    for key in sorted(stat_code):
        print("{}: {}".format(key, stat_code[key]))


if __name__ == "__main__":
    import sys

    size = 0
    stat_code = {}
    val_cod = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, stat_code)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in val_cod:
                    if stat_code.get(line[-2], -1) == -1:
                        stat_code[line[-2]] = 1
                    else:
                        stat_code[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, stat_code)

    except KeyboardInterrupt:
        print_stats(size, stat_code)
        raise
