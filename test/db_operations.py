import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',
    ( 'Uff', 4 ) )
cur.execute('INSERT INtO Tracks (title, plays) VALUES ( ?, ? )',
    ( 'Miau', 5 ) )
conn.commit()

print ('Tracks:')
# stores all rows in the cursor and with the for loop they will be printed
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays = 20')
cur.execute('UPDATE Tracks SET plays = 16 WHERE title = "My Way"')
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('Test', 10) )
conn.commit()

print ('Tracks:')
# stores all rows in the cursor and with the for loop they will be printed
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

cur.close()
