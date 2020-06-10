import io
import os
import csv
import json

files_folder = 'json'

dorms = ['Sally Ride', 'Casa Zapata']

files = os.listdir(files_folder)
files.sort()

for filename in files:
    students = []
    with open(f"{files_folder}/{filename}", 'r') as file:
        text = json.load(file)['text']

        lines = text.split('\n')

        for line in lines:
            words = line.split(' ')

            if len(words) > 1 and line not in dorms:
                students.append([line])

        with open('students_2023.csv', mode='a') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(students)

'''
https://profiles.stanford.edu/search?q=Moritz%20Stephan
'''
