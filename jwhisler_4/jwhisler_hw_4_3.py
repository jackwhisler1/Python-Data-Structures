"""
Jon Whisler

Class: CS 521 - Fall

Date: 9/27/2025

Homework Problem # 4_3

Description: Stores health data in a dictionary representing each patient
"""
import random


def get_new_id():
    return (str(random.randint(000, 999)).zfill(3) +
            '-' +
            str(random.randint(1000, 9999)))


patient_ids = []
for i in range(30):
    id = get_new_id()
    while id in patient_ids:
        id = get_new_id()
    patient_ids.append(id)

try:
    patients = []
    with open('heart_failure_clinical_records_dataset.csv') as f:
        file_headers = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            patients.append(dict(zip(file_headers, values)))
except FileNotFoundError:
    print('no file found')

mathced_patient_records = dict(zip(patient_ids, patients))
print(mathced_patient_records[patient_ids[24]])
