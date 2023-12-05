#!/usr/bin/python3
'''
    Log parsing
'''


def print_metrics(file_size, status_code_counts):
    '''
        reads stdin line by line
    '''
    print("File size: {}".format(file_size))
    for code, count in sorted(status_code_counts.items()):
        print("{}: {}".format(code, count))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_code_counts = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(total_size, status_code_counts)
                line_count = 1
            else:
                line_count += 1

            words = line.split()

            try:
                total_size += int(words[-1])
            except (IndexError, ValueError):
                pass

            try:
                if words[-2] in valid_codes:
                    status_code_counts
                    [words[-2]] = status_code_counts.get(words[-2], 0) + 1
            except IndexError:
                pass

        print_metrics(total_size, status_code_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_code_counts)
        raise
