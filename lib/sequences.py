#!/usr/bin/env python3

      


def print_fibonacci(length):
    fib = []  # this is your Fibonacci list

    if length == 0:
        print(fib)
        return
    elif length == 1:
        fib.append(0)
    elif length >= 2:
        fib = [0, 1]
        for _ in range(2, length):
            next_num = fib[-1] + fib[-2]
            fib.append(next_num)

    print(fib)
 
