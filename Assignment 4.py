# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:18:34 2023

@author: SRIMOYEE
"""

# Collect student information
student_name = input("Enter student's name: ")
student_age = input("Enter student's age: ")
student_grade = input("Enter student's grade: ")
# Create a dictionary to store student information
student_data = {
    'Name': student_name,
    'Age': student_age,
    'Grade': student_grade
}
# Write data to a CSV file
import csv

with open('student_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=student_data.keys())
    writer.writeheader()
    writer.writerow(student_data)