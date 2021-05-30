from loader import load_db
from model import Book
from render import render_table
from repository import BookRepository


def main():
    books = load_db('./book-db.csv')
    # TODO: query from ,  , date range
    repository = BookRepository(books)
    while True:
        result = []
        print('Welcome to Kamar Tarj Book Library\n')
        print('[1] Search by author name')
        print('[2] Search by length of book')
        print('[3] Search by recent year')
        print('[q] to quit program\n')
        menu_select = input('Please select search mode: ')
        if menu_select == '1':
            author_name = input('Please type author name: ')
            result: list[Book] = repository.find_by_author(author_name)
            print('Searching for book(s) with author name "'+author_name+'"')
        elif menu_select == '2':
            length = int(input('Please type length of book: '))
            result: list[Book] = repository.find_by_hardest(length)
            print('Searching for book(s) with length more than '+str(length)+' page(s)')
        elif menu_select == '3':
            year = int(input('Please type number of year: '))
            result: list[Book] = repository.find_by_recent(year)
            print('Searching for book(s) published in last '+str(year)+' year(s)')
        elif menu_select == 'q':
            print('Good bye Dr.Strange')
            break
        if result:
            render_table(result)
            input('Press Enter to continue...')
        else:
            print('Please try again...')
    pass


if __name__ == '__main__':
    main()
