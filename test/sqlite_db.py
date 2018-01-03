import sqlite3

# connect, creates a "connection" with the file music.sqlite3 in the
# dictionary. If no such file exists, it will be created
# The reason its called connection, because often the database is
# stored on a seperate server. In our case its simply in the current folder
conn = sqlite3.connect('music.sqlite3')

# Calling cursor() is very similar conceptually to calling
# open() when dealing with text files.
cur = conn.cursor()

# Once we have the cursor, we can begin to execute
# commands on the contents of the database using the execute() method.
cur.execute('DROP TABLE IF EXISTS Tracks ')

# We always need to specify the columns and respective datatypes
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()
