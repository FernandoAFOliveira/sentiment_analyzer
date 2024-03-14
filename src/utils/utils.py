#utils.utils.py

import csv
import os

def list_csv_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

def list_columns_in_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return reader.fieldnames
