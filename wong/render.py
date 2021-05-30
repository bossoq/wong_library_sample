from rich.console import Console
from rich.table import Table

from model import Book


def render_table(books: list[Book]) -> None:
    table = Table(title="Kamar Tarj Library")

    table.add_column('Name', justify='right', style='cyan')
    table.add_column('Author', justify='right', style='red')
    table.add_column('Length', justify='center', style='blue')
    table.add_column('Publication Date', justify='right', style='yellow')

    for book in books:
        table.add_row(book['name'], book['author'],
                      str(book['length']),
                      book['publication_date'].strftime('%B %d, %Y'))

    console = Console()
    console.print(table)
