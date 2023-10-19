# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:56:30 2023

@author: SRIMOYEE
"""

def most_frequent(input_string):
    # Create an empty dictionary to store letter frequencies
    letter_count = {}
    
    # Remove spaces and convert the input string to lowercase
    input_string = input_string.replace(" ", "").lower()

    # Count the frequency of each letter
    for letter in input_string:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1

    # Sort the dictionary by frequency in decreasing order
    sorted_letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))

    # Print the result
    for letter, count in sorted_letter_count.items():
        print(f"{letter} = {count:02d}")

# Input string
input_string = "Mississippi"

# Call the function
most_frequent(input_string)