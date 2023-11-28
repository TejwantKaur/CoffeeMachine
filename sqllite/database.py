import sqlite3

# connect to database
conn = sqlite3.connect('student.db')

# create a cursor
c = conn.cursor()

# create a Table
# c.execute("""
#     CREATE TABLE STUDENTS(
#         FIRST_NAME TEXT,
#         LAST_NAME TEXT,
#         EMAIL TEXT
#     )
# """)

# c.execute("INSERT INTO STUDENTS VALUES('RANBIR', 'SINGH', 'ranbircipet@gmail.com')")

# many_students = [
#     ('RAVI', 'DUBEY', 'ravi@codemy.com'),
#     ('TOM', 'KATE', 'kate@codemy.com'),
#     ('SHARU', 'BOTT', 'sharu@codemy.com'),
# ]
#
# c.executemany("INSERT INTO STUDENTS VALUES(?,?,?)", many_students)

# execute query
# c.execute("SELECT * FROM STUDENTS")
# fetchone(), fetchmany(3), fetchall()

# print(c.fetchone())
# print(c.fetchmany(3))
# print(c.fetchall())

# items = c.fetchall()
# print("NAME" + "\t\t\t" + "EMAIL")
# print("------" + "\t\t\t" + "------")
# for item in items:
#     # print(item)
#     print(item[0] + " " + item[1] + "\t" + item[2])

# c.execute("SELECT rowid,* FROM STUDENTS")
# # rowid --> already exists as a primary key

# c.execute("SELECT * FROM STUDENTS WHERE LAST_NAME = 'KAUR' ")
# c.execute("SELECT * FROM STUDENTS WHERE AGE >= 21 ")
c.execute("SELECT * FROM STUDENTS WHERE EMAIL LIKE '%@codemy.com' ")















items = c.fetchall()
for item in items:
    print(item)

# print("Command executed successfully")
# commit
conn.commit()
# close connection
conn.close()
