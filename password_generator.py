import string
import random

alpha_lower = string.ascii_lowercase
alpha_upper = string.ascii_uppercase
nums = string.digits
symbols = string.punctuation

while True:
    print('\n Which Type of Password you want'
            '\n 1) Regular Password'
            '\n 2) Secure Password'
            '\n 3) Exit')
    choice = int(input('\nEnter Your Choice [1/2/3]: '))

    if choice == 1:
        reg_pass_len = int(input('Enter  Password Length :'))

        regular_password = []

        regular_password.extend(list(alpha_lower))
        regular_password.extend(list(alpha_upper))

        random.shuffle(regular_password)

        print('Your Password is : ')
        print(''.join(regular_password[0:reg_pass_len]))

    elif choice == 2:
        
        SECURE = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'))

        def securePassword(password):
            for a,b in SECURE:
                password = password.replace(a,b)
            return password
            
        if __name__ == "__main__":
            password = input('Enter Your Password \n')
            password = securePassword(password)
            print(f"Your secure Password is {password}")


    elif choice == 3:
        break

    else:
        print('Invalid Choice')