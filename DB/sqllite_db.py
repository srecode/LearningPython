import sqlite3

con = sqlite3.connect('sqlite3.db')

cur = con.cursor()

# cur.execute("CREATE TABLE movie3(title, year, score)")

res = cur.execute("SELECT name FROM sqlite_master")

res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

con.commit()

res = cur.execute("SELECT score FROM movie")
results = res.fetchall()

# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")

print(results   )