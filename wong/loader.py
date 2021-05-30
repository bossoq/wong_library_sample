# standard library
import csv
from datetime import datetime

# 3rd party package

# local package
from model import Book


def load_db(filename: str) -> list[Book]:
    books = []

    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            row['length'] = int(row['length'])
            row['publication_date'] = datetime.strptime(row['publication_date'], '%B %d, %Y').date()
            books.append(row)

    return books
