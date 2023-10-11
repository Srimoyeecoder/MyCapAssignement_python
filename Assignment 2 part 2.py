# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:31:51 2023

@author: SRIMOYEE
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

# Change the value of 'n' to generate Fibonacci numbers up to the desired limit
n = 14  # Example: To generate the first 14 Fibonacci numbers
fib_numbers = fibonacci(n)
print(fib_numbers)