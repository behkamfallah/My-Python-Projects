# Our text file is large, so we have to use 'yield'.
def check_password(user_input: str):
    def csv_reader(filename):
        with open(filename, encoding='utf8') as pass_list:
            for each_line in pass_list:
                yield each_line.strip()

    ''' 
    Here we open the file and check if it is equal to user input or not.
    
    Param row_count shows the rank of code!
    '''
    row_count = 0
    for row in csv_reader("15M.txt"):
        row_count += 1
        if row == user_input:
            print(f"{row}: ⛔ Don't use this password! (#{row_count})")
            return
    print(f'{user_input}: ✅ (Safe!)')


def main():
    # Get input from user
    while True:
        print('--------------------------------')
        print('Type exit if you want to quit.')
        print('--------------------------------')
        user_input = input('Enter your Password: ')
        if user_input == '':
            print('Please enter your password!')
            continue
        elif user_input == 'exit':
            print('--------------------------------')
            print('Thanks for using! Stay safe!')
            break
        else:
            check_password(user_input)


if __name__ == '__main__':
    main()