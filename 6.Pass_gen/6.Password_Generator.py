import string
import secrets
import random

def generate_password(length, upper_case, symbols):
    combination = string.ascii_lowercase + string.digits
    if upper_case:
        combination += string.ascii_uppercase
    if symbols:
        combination += string.punctuation
    
    combination_length = len(combination)
    password = ''

    for _ in range(2):
        password += string.ascii_uppercase[secrets.randbelow(len(string.ascii_uppercase))]
    for _ in range(2):
        password += string.punctuation[secrets.randbelow(len(string.punctuation))]
    for _ in range(length - 4):
        password += combination[secrets.randbelow(combination_length)]

    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    print(f'Your password is: {password}')

if __name__ == '__main__':
    print('--------------------------------------')
    print('Welcome to Secure Password Generator.')
    print('--------------------------------------')
    while True:
        try:
            user_input = int(input('How long your password should be? (6 to 128) -> '))
            if user_input < 6 or user_input > 128:
                print('Please enter a number between 6 and 128.')
                continue
            else:
                print('--------------------------------------')
                generate_password(user_input, True, True)
                print('--------------------------------------')
                user_input = input('Do you want to generate another one? [yes/any key to exit]: ')
                if user_input.lower() == 'yes':
                    continue
                else:
                    break
        except ValueError as e:
            print('Please enter a number!')
            continue
    