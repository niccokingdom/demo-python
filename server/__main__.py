import os
import sys
sys.path.append('.')

from server.webapp import flaskapp, database, cursor, TEMPLATES
from server.models import *
from server.routes import *

default_books = [
    ("The Hobbit", "JRR Tolkien", True),
    ("The Fellowship of the Ring", "JRR Tolkien", True),
    ("The Eye of the World", "Robert Jordan", False),
    ("A Game of Thrones", "George R. R. Martin", True),
    ("The Way of Kings", "Brandon Sanderson", False)
]

api_key = "sk_live_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0"


if __name__ == "__main__":
    cursor.execute(
        '''CREATE TABLE books (name text, author text, read text)'''
    )

    for bookname, bookauthor, hasread in default_books:
        try:
            cursor.execute(
                'INSERT INTO books values (?, ?, ?)',
                (bookname, bookauthor, 'true' if hasread else 'false')
            )

        except Exception as err:
            print(f'[!] Error Occurred: {err}')

    flaskapp.run('0.0.0.0', debug=bool(os.environ.get('DEBUG', False)))
    
    cursor.close()
    database.close()
