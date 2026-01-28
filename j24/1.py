import sqlite3
connection = sqlite3.connect("./storeDB.db")
cursor = connection.cursor()
mamad = """
CREATE TABLE IF NOT EXISTS users (
userId INTEGER primary key not null ,
name VARCHAR (60),
family VARCHAR (60),
email VARCHAR (60),
adress text
);
"""
cursor.execute(mamad)
connection.commit()

# sql = """
# insert into users
# (userId, name, family, email, adress)
# values
# (1, 'ali', 'ahmadi', 'a@yahoo.com', 'tehran, tehran')
# """

# cursor.execute(sql)
# connection.commit()

cursor.execute("select * from users")
connection.commit()

connection.close()
