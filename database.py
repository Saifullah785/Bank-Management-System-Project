# Database Management Banking
import mysql.connector as sql


mydb = sql.connect(

    host="localhost",
    user="root",
    password="",
    database="bank"

)
cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def create_customer_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers 
               (username VARCHAR(20),
               password VARCHAR(20),
               name VARCHAR(25),
               age INTEGER,
               city VARCHAR(20),
               account_number INTEGER,
               status BOOLEAN)
 

''')

mydb.commit()
if __name__ == "__main__":
    create_customer_table()
    