# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:03:08 2023

@author: SRIMOYEE
"""

def get_positive_numbers(input_list):
    positive_numbers = [num for num in input_list if num > 0]
    return positive_numbers

# Example usage
list1 = [12, -7, 5, 64, -14]
output1 = get_positive_numbers(list1)
print("Input:", list1, "Output:", output1)

list2 = [12, 14, -95, 3]
output2 = get_positive_numbers(list2)
print("Input:", list2, "Output:", output2)
              