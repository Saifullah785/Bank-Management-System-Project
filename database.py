# Database Management Banking
import mysql.connector as sql

# create a connection to the database using mysql connector
# create a cursor object to execute the queries
# create a database and a table
#create a table for customers

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

# create a table for customers
def create_customer_table():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers 
               (username VARCHAR(20) NOT NULL,
               password VARCHAR(20) NOT NULL,
               name VARCHAR(25) NOT NULL,
               age INTEGER NOT NULL,
               city VARCHAR(20) NOT NULL,
               balance INTEGER NOT NULL ,
               account_number INTEGER UNIQUE NOT NULL,
               status BOOLEAN NOT NULL)
 

''')

mydb.commit()
if __name__ == "__main__":
    create_customer_table()
    