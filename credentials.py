import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  #port="3306",
  user="root",
  passwd="1234",
  #auth_plugin="mysql_native_password"
)



print(mydb)


cursor = mydb.cursor()
cursor.execute("CREATE TABLE customers (name VARCHAR(255), id VARCHAR(255))")
SQL = "SELECT * FROM sys.customers"
cursor.execute(SQL)
records = cursor.fetchall()


#df = pd.DataFrame(records)