
import sqlite3

conn = sqlite3.connect("test.db")
c    = conn.cursor()

books = [(11, 1, 'Cook Recipe', 3.12, 1),
            (12, 3, 'Python Intro', 17.5, 2),
            (13, 2, 'OS Intro', 13.6, 2),
           ]

# execute "INSERT"
c.execute("INSERT INTO category VALUES (21, 1, 'kitchen')")

# using the placeholder
#c.execute("INSERT INTO category VALUES (?, ?, ?)", [(22, 2, 'computer')])

# execute multiple commands
c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)

conn.commit()
conn.close()