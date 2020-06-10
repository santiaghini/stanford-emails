import io
import os
import csv
import json
import time
import requests

csv_name = 'students_2023.csv'
new_csv_name = '2023.csv'
base_url = 'https://profiles.stanford.edu/proxy/api/cap/search/keyword?q='

students = []
new_students = []

student_to_resume = 'Simon Camacho'

resume = False

with open(csv_name, mode='r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for student in csv_reader:
        students.append(student)

    for line in students:

        student = line[0]

        if (student != student_to_resume and resume == False):
            continue
        elif student == student_to_resume:
            resume = True

        print(student)

        query = '%20'.join(student.split())

        print(query)

        # sending get request and saving the response as response object
        r = requests.get(url=base_url + query)

        # extracting data in json format
        data = r.json()

        if data['ui'].get('exactNameMatches', None):
            email = data['ui']['exactNameMatches'][0]['email']
        else:
            email = data['ui']['keywordMatches'][0]['email']

        print(email)

        student_words = student.split()

        first_name = student_words[0]
        rest = ' '.join(student_words[1:])

        new_student = [first_name, rest, email]

        new_students.append(new_student)

        with open(new_csv_name, mode='a') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows([new_student])


# send request for every name
# https://profiles.stanford.edu/search?q=Moritz%20Stephan
