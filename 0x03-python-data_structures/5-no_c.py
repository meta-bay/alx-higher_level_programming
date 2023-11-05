#!/usr/bin/python3

def no_c(my_string):
    string_arr = []
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            string_arr.append(i)
    result_string = "".join(string_arr)
    return result_string
