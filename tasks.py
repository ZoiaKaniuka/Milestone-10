import csv
from collections import defaultdict
from datetime import datetime

def read_employees(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def count_birthdays_by_month(employees):
    birthday_count = defaultdict(int)
    for emp in employees:
        try:
            date = datetime.strptime(emp["birthdate"], "%Y-%m-%d")
            birthday_count[date.strftime("%B")] += 1
        except Exception:
            raise ValueError(f"Corrupted birthdate: {emp}")
    return birthday_count
