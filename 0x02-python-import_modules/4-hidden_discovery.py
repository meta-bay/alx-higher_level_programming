#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    key_list = dir(hidden_4)
    for i in key_list:
        if not i.startswith("__"):
            print(i)
