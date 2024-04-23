from random import randint

#variables
lower_number, higher_number = 1, 10
random_number = randint(lower_number, higher_number)
shots = 0
max_shots = higher_number // 3
min_shots = lower_number


#instructions for player
print(f"Guess the number in the range from {lower_number} to {higher_number}.")
print('How many shots do you want to have?')

while True:
    try:
        shots = int(input(f"Enter a number between {min_shots} and {max_shots}: "))
        if shots > max_shots or shots < min_shots:
            print('Please enter a number in the given range.')
            continue #This line takes us to the first of while loop!
        else:
            break
    except:
        print('Please enter a number in the given range.')

shots_remainig = shots
while True:
    if shots_remainig != 1:
        print(f"Number of shots remaining: {shots_remainig}")
    else:
        print('This is your only and last chance!')
    
    try:
        user_guess = int(input(f"Please enter your guess: "))
    except ValueError as e:
        print('Please enter a valid number!')
        continue #This line takes us to the first of while loop!
    
    if shots_remainig > 1:
        shots_remainig -= 1
        if user_guess > random_number:
            print('Target number is lower.')
        elif user_guess < random_number:
            print('Target number is higher.')
        else:
            print(f"You guessed it right!!!!! {user_guess} is your lucky number!")
            break
    else:
        shots_remainig -= 1
        if user_guess == random_number:
            print(f"You guessed it right!!!!! {user_guess} is your lucky number!")
            break
        print(f"You could not guess it! The number was {random_number}.")
        print('Wish you luck next time!')
        break