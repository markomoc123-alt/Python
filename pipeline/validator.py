"""Check rows before turning them into transactions."""

from pipeline.schema import TransactionRecord


def digits(text):
    # This example accepts whole numbers of up to eight digits.
    valid = len(text) > 0 and len(text) <= 8
    for character in text:
        if character not in "0123456789":
            valid = False
    return valid


def valid_date(text):
    valid = False
    parts = text.split("-")
    if len(parts) == 3 and [len(part) for part in parts] == [4, 2, 2]:
        if digits(text.replace("-", "")):
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            # February has 29 days in a leap year.
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                days[1] = 29
            if year > 0 and month >= 1 and month <= 12:
                valid = day >= 1 and day <= days[month - 1]
    return valid


def validate(rows):
    records = []
    for row in rows:
        fields = []
        if type(row) == str:
            fields = [value.strip().upper() for value in row.split("|")]
        valid = len(fields) == 7
        if valid:
            valid = (fields[0] in ["A", "B"] and valid_date(fields[1])
                     and fields[2] in ["GOLD", "REGULAR"]
                     and digits(fields[3]) and digits(fields[4])
                     and digits(fields[5]) and fields[6] in ["YES", "NO"])
        if valid:
            valid = int(fields[3]) > 0
        if valid:
            records.append(TransactionRecord(fields))
        else:
            print("Rejected:", row)
    return records
