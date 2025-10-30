# !python3/bin/bash

from fib import fib

def print_n_fib(n):
    for i in range(n):
        print(fib(i))

if __name__ == "__main__":
    print_n_fib(5)