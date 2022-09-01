import mysql.connector

conn = mysql.connector.connect(user='root',password='ABC123',host='127.0.0.1',database='mysql')

cursor = conn.cursor()
cursor.execute("SELECT DATABASE()")


data = cursor.fetchone()
print("connection established to:",data)

conn.close()