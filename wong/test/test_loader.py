from datetime import datetime
from ward import test

from loader import load_db


@test('test load db should return list of books')
def _():
    expected = 20
    actual = load_db('./book-db.csv')
    assert expected == len(actual)


@test('test length should be integer')
def _():
    expected = 301
    actual = load_db('./book-db.csv')
    assert expected == actual[0]['length']


@test('test publication date should be date')
def _():
    expected = datetime(2017, 10, 25).date()
    actual = load_db('./book-db.csv')
    assert expected == actual[0]['publication_date']
