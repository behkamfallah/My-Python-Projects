from random import randint

def roll_dice(amount = 2):
    if amount <= 0:
        raise ValueError
    
    rolls = []
    for i in range(amount):
        rnd_roll = randint(1, 6)
        rolls.append(rnd_roll)
    
    return(rolls)
    
def main():
    print("""----------------------------------------------
Type exit when you want to close the program.
----------------------------------------------""")
    while True:
        try:
            user_input = input('How many dice would you like to roll? : ')
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break
            
            result = roll_dice(int(user_input))
            print(*result, sep =', ')
            print(f"Sum of the random numbers are: {sum(result)}")
        except ValueError:
            print('Please enter a valid number!')

if __name__ == '__main__':
    main()