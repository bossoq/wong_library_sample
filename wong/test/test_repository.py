from datetime import datetime
from ward import test

from repository import BookRepository


@test('test find by author should return list of books')
def _():
    books = [
        {
            'name': 'The Gatuk book',
            'author': 'Gatuk'
        },
        {
            'name': 'The Human book',
            'author': 'Human'
        }
    ]

    repository = BookRepository(books)
    actual = repository.find_by_author(name='Gatuk')
    assert 1 == len(actual)
    assert 'Gatuk' == actual[0]['author']


@test('test find by hardest should return list of books')
def _():
    books = [
        {
            'name': 'The Gatuk book',
            'length': 300
        },
        {
            'name': 'The Human book',
            'length': 280
        }
    ]

    repository = BookRepository(books)
    actual = repository.find_by_hardest(length=300)
    assert 1 == len(actual)
    assert 300 == actual[0]['length']


@test('test find by recent should return list of books')
def _():
    books = [
        {
            'name': 'The Gatuk book',
            'publication_date': datetime(2020, 10, 25).date()
        },
        {
            'name': 'The Human book',
            'publication_date': datetime(2017, 10, 25).date()
        }
    ]

    repository = BookRepository(books)
    actual = repository.find_by_recent(year=2)
    assert 1 == len(actual)
    assert datetime(2020, 10, 25).date() == actual[0]['publication_date']
