import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  passwd="1234"
)


print(mydb)

SQL2 = "CREATE TABLE sys.customers (name VARCHAR(255), id VARCHAR(255))"
SQL3 = "INSERT INTO sys.customers VALUES (%s, %s)"
val = ('1','abc')
SQL1 = "SELECT * FROM sys.customers"
cursor = mydb.cursor()
#cursor.execute(SQL1)
cursor.execute(SQL1)
#mydb.commit()
records = cursor.fetchall()
print(records)

