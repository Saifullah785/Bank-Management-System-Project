
from register import *
from bank import *



# Set initial status to False
status = False
print('Welcome to PAK banking Project')

# Main loop for Sign Up/In
while True:
    try:
        register = int(input('1. Sign Up\n2. Sign In\n'))

        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                status = True
                break

        else:
            print('Please Enter valid input from Options')
    

    except ValueError:
        print('Invalid input Try Again with Numbers')


# Fetch account number after successful sign-in

account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")

# Banking service loop
#
while status:
    print(f'Welcome {user.capitalize()} Choose your Banking Service\n')
    try:
        facility = int(input(' 1. Balance Enquiry\n 2. Cash Deposit\n 3. Cash Withdraw\n 4. Fund Transfer\n'))

        if facility >= 1 and facility <= 4:
            if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.balance_enquiry()
            if facility == 2:
                while True:
                    try:
                        amount = int(input('Enter Amount to Deposit: '))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break

                    except ValueError:
                        print('Enter Valid input ie. Number')   
                        continue
               
                
            elif facility == 3:
                while True:
                    try:
                        amount = int(input('Enter Amount to Withdraw: '))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break

                    except ValueError:
                        print('Enter Valid input ie. Number')   
                        continue
                
                
            elif facility == 4:
                while True:
                    try:
                        receive = int(input('Enter Receiver Account Number: '))
                        amount = int(input('Enter Money to Transfer: '))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fund_transfer(receive, amount)
                        mydb.commit()
                        break

                    except ValueError:
                        print('Enter Valid input ie. Number')   
                        continue

        else:
            print('Please Enter valid input from Options')
            continue
    

    except ValueError:
        print('Invalid input Try Again with Numbers')
        continue