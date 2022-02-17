import sqlite3

from sqlite3 import Error

def sql_connection():
    try:
        conn=sqlite3.connect('Studentdatabase.db')
        return conn
    except Error:
        print(Error)

def sql_table(conn):
    cursorObj = conn.cursor()
    # cursorObj.execute("CREATE TABLE students(student_id n(5), name char(30), marks n(7),per devimal(3,2)) ;")
    # cursorObj.executescript("""
    # INSERT INTO students values(10,'Nani',234,67.7);
    # INSERT INTO students values(20,'Nethra',300,87.7);
    # INSERT INTO students values(40,'John',434,97.7);
    # """)

    conn.commit()
    cursorObj.execute("SELECT * from students")

    rows = cursorObj.fetchall()
    print("Student details:")
    for row in rows:
        print(row)

sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")

def sql_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("SELECT * from students")
    rows = cursorObj.fetchall()
    print("student Detailes:")
    for row in rows:
        print(row)
    print("\n Update id to 40  where student_id  is 30:")
    sql_update_query = """Update students set student_id = 50 where name='John'"""
    cursorObj.execute(sql_update_query)
    conn.commit()
    print("Record updated successfully")
    cursorObj.execute("SELECT * from students")
    rows = cursorObj.fetchall()
    print("\n After updating student Detailes:")
    for row in rows:
        print(row)

sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")

def sql_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("SELECT * from students")
    rows = cursorObj.fetchall()
    print("Student Detailes:")
    for row in rows:
        print(row)
    print("\n Delete students of student_id=10:")
    student_id = 10
    cursorObj.execute("""
    DELETE FROM students
    where student_id = ?""",(student_id,))
    conn.commit()
    cursorObj.execute("SELECT * FROM students")
    rows = cursorObj.fetchall()
    print("\n after updating student detailes:")
    for row in rows:
        print(row)
sqlite_conn = sql_connection()
sql_table(sqlite_conn)
if(sqlite_conn):
    sqlite_conn.close()
    print("\n The Sqlite connection is closed.")
