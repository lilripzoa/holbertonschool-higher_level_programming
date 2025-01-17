#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print(f"{num_arguments} argument{'s' if num_arguments > 1 else ''}:")

        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
