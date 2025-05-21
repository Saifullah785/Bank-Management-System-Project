
from register import *
print('Welcome to PAK banking Project')
while True:
    try:
        register = int(input('1. Sign Up\n2. Sign In\n'))

        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                SignIn()

        else:
            print('Please Enter valid input from Options')
    

    except ValueError:
        print('Invalid input Try Again with Numbers')
