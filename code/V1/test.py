import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE PHONEBOOK")

cursor.executescript("""CREATE TABLE PHONEBOOK(NAME CHAR, PHONE CHAR, EMAIL CHAR PRIMARY KEY);
               CREATE TABLE TEST(NAME CHAR, PHONE CHAR, EMAIL CHAR);""")

cursor.execute("INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL) VALUES(?, ?, ?)",('김김김', '010-111-1111', 'dafuoawo23@gmail.com'))

cursor.execute("INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL) VALUES(?, ?, ?)", ('이이이', '010-1231-1121', 'adsfnjfsn33334@gmail.com'))

cursor.execute("INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL) VALUES(?, ?, ?)",('한한한', '010-111-1111', 'dsajfnasjkn234@gmail.com'))

id = cursor.lastrowid
print(id)

conn.commit()

cursor.execute("SELECT NAME, PHONE, EMAIL FROM PHONEBOOK")

rows = cursor.fetchall()
for row in rows:
    print("NAME: {0}, PHONE: {1}, EMAIL: {2}".format(row[0], row[1], row[2]))

cursor.close()
conn.close()