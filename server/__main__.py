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

FAKE_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAyZ9V1aB5s4kY+p2F/L/C/g5n2kX/v8b3j4h5g6t7y8i9o0k7l6
... (this is just random text for the example) ...
a9b8c7d6e5f4g3h2i1j0k9l8m7n6o5p4q3r2s1t0u9v8w7x6y5z4a3b2c1d0e9f8g7
-----END RSA PRIVATE KEY-----
"""

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
