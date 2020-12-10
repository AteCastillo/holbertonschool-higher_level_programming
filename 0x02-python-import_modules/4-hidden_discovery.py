#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for name in dir(hidden_4):  # name is every name of the dir
        if name[:2] != "__":  # it does not include character 2
            print("{}".format(name))
