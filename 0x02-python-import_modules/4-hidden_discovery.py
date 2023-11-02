#!/usr/bin/python3

if __name__ == "__main__":
    key_list = dir("hidden_4.pyc")
    for i in key_list:
        if i.startswith("__"):
            continue
        print(i)
