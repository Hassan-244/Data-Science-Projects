import sqlite3

conn=sqlite3.connect("student.db")

cursor=conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY ,
        name TEXT,
        marks INTEGER,
        grade TEXT 
)                     
""")

students_data=[
    (1, "Ali", 85, "A"),
    (2, "Sara", 65, "C"),
    (3, "Ahmed", 92, "A"),
    (4, "Hassan", 97, "A"),
    (5, "Ayesha", 88, "A")
]

cursor.executemany(
    "INSERT OR REPLACE INTO students VALUES(?,?,?,?)",
    students_data
)

conn.commit()

print("\n📌 ALL STUDENTS")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

print("\n📌STUDENT WITH GRADE A:")
cursor.execute("SELECT name,marks from students where grade='A'")
print(cursor.fetchall())

print("\n📌 AVERAGE MARKS: ")
cursor.execute("SELECT AVG(marks) from students")
print(cursor.fetchone())

print("\n📌 HIGHEST MARKS: ")
cursor.execute("SELECT MAX(marks) from students")
print(cursor.fetchone())

print("\n📌 STUDENT WITH MARKS >80: ")
cursor.execute("SELECT name,marks from students where marks>80")
print(cursor.fetchall())

conn.close()