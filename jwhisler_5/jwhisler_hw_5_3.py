"""
Jon Whisler

Class: CS 521 - Fall

Date: 10/3/2025

Homework Problem # 5_3

Description: Returns first and last patient from provided file
"""


def process_patient_record(record):
    """Accepts a line of a patient's record for csv file and returns a patient dict object"""
    keys = [
        'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
        'ejection_fraction', 'high_blood_pressure', 'platelets',
        'serum_creatinine', 'serum_sodium', 'sex', 'smoking',
        'time', 'DEATH_EVENT'
    ]
    values = record.strip().split(',')
    patient_dict = dict(zip(keys, values))
    return patient_dict


if __name__ == '__main__':
    patient_records = {}
    id = 1000
    try:
        with open('heart_failure_clinical_records_dataset.csv') as file:
            lines = file.readlines()[1:]

            for i, l in enumerate(lines):
                patient_id = id + i
                patient_data = process_patient_record(l)
                patient_records[patient_id] = patient_data

        first_id = min(patient_records.keys())
        last_id = max(patient_records.keys())

        print(patient_records[first_id])
        print(patient_records[last_id])
    except Exception as e:
        print("Err: " + {e})
