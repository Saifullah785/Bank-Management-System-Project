# Bank Services
from database import *
import datetime

# creating a class Bank
# which will have all the methods
# for banking services
# like deposit, withdraw, fund transfer
# and balance enquiry
# and also create a transaction table   
# for each user
# for transaction history
# and also create a transaction table
class Bank:

    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number



    # creating a transaction table
    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction "
                 f"( timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER)")
    

    # creating a balance enquiry method which will show the balance of the user
    def balance_enquiry(self):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}' ;")
        print(f"{self.__username} Balance is {temp[0][0]}")




    # creating a deposit method which will deposit the amount
    def deposit(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}' ;")
        test = amount + temp[0][0]
        db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}';")
        self.balance_enquiry() 
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}');")
        
        print(f"{self.__username} Amount Deposited Successfully in your Account {self.__account_number}")
        

    # creating a withdraw method which will withdraw the amount
    def withdraw(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}' ;")
        if amount > temp[0][0]:
            print(f"Insufficient Balance please deposit some amount")

        else:
            test = temp[0][0] - amount
            db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}';")
            self.balance_enquiry() 
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Amount Withdraw',"
                     f"'{amount}'"
                     f")")

            print(f"{self.__username} Amount Withdrawn Successfully from your Account {self.__account_number}")


    # creating a fund transfer method which will transfer the amount from one account to another
    def fund_transfer(self, receive, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}' ;")
        if amount > temp[0][0]:
            print(f"Insufficient Balance Please Deposit Some Amount")

        else:
            temp2 = db_query(f"SELECT balance FROM customers WHERE account_number = '{receive}' ;")

            test1  = temp[0][0] - amount
            test2 = amount + temp2[0][0]

        
            db_query(f"UPDATE customers SET balance = '{test1}' WHERE username = '{self.__username}';")
            db_query(f"UPDATE customers SET balance = '{test2}' WHERE account_number = '{receive}';")
            self.balance_enquiry() 
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Fund Transfer -> {receive}',"
                     f"'{amount}'"
                     f")")

            print(f"{self.__username} Amount Transferred Successfully from your Account {self.__account_number}")