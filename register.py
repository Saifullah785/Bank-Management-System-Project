# user Registration Sign In  Sign Up
from database import *
from customer import *

import random

def SignUp():
    username = input('Create Username: ')
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print('Username already exists')
        SignUp()
    else:
        print('Username is available Please proceed')
        password = input('Enter your Password: ')
        name = input('Enter your Name: ')
        age = input('Enter your Age: ')
        city = input('Enter your City: ')
        while True:

            account_number = random.randint(  1000000000, 9999999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
              continue
            else:
                print(account_number)
                break
        
    cobj = Customer(username, password, name, age, city, account_number, True)
    cobj.createuser()


def SignIn():
        
        username = input('Enter your Username: ')
       
        temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
        if temp:
            while True:
               password = input(f'Welcome {username.capitalize()}, Enter your Password: ')
               temp = db_query(f"SELECT password FROM customers WHERE username = '{username}' ;")
               if temp[0][0] == password:
                   print ('Sign In Successful')
                   break
               else:
                   print ('Wrong Password Try Again')
                   continue
        else:
            print("Enter Correct Username")
            SignIn()
                   

          