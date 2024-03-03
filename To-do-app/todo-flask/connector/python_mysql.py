import mysql.connector

conn=mysql.connector.connect(host='localhost', username='root', password='Root@123', database='to-do-app')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("Connection successfully created!")