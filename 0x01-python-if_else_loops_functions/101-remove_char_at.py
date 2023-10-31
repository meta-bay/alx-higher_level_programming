#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        new = ''
        for c in str:
            new += c if c != str[n] else ''
        return new
    else:
        return str
