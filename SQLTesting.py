import sqlite3
conn = sqlite3.connect('Scores.db')

c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE Scores(PlayerName text, Turns real)''')

# Insert a row of data
c.execute("INSERT INTO Scores VALUES ('COLIN',35)")

for row in c.execute('SELECT * FROM Scores ORDER BY Turns'):
    print(row)
# Save (commit) the changes
conn.commit()