import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    major TEXT,
    gpa REAL
)
""")
conn.commit()

cursor.execute(
    "INSERT INTO student (name, major, gpa) VALUES (?, ?, ?)",
    ("Reza", "Phisics", 19)
)
conn.commit()

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("----------------")

cursor.execute(
    "UPDATE student SET gpa=? WHERE name=?",
    (17.75, "Reza")
)
conn.commit()

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("----------------")

cursor.execute("DELETE FROM student WHERE id=?", (1,))
conn.commit()

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("----------------")