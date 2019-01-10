import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)
user = (1, 'josh', 'asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
#Insert single row
cursor.execute(insert_query, user)
users = [
    (2, 'jo', 'asdf'),
    (3, 'anne', 'asdf'),
    (4, 'joseph', 'asdf')
]
#insert many users
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()