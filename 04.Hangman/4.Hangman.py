from random import choice

def run_game():
    word_list = []
    try:
        with open('wordlist.txt') as dictionary:
            for row in dictionary:
                word_list.append(row.strip())
    except FileNotFoundError:
        print("File 'wls.txt' not found.")
    except Exception as e:
        print("An error occurred:", e)

    while True:
        word = choice(word_list) #picks a random one

        username = input('What is your name? -> ')
        print(f"Welcome to hangman {username}.")

        guessed_letters = ''
        tries = len(word) - 1
        
        blanks = len(word)
        while tries > 0:
            #keeps the number of not guessed yet characters.
            
            
            if tries > 1:
                print(f"You have {tries} tries remaining.")
            else:
                print('This is your last chance!')
            
            print('Word: ', end='')
            for char in word:
                if char in guessed_letters:
                    print(char, end='')
                else:
                    print('_ ', end='')
            print() #prints an empty line.

            guess = input('Enter a letter: ')
            if len(guess) == 1:
                if guess in guessed_letters:
                    print(f'You already said: "{guess}". Please try again!')
                    continue
                else:
                    tries -= 1
                    guessed_letters += guess
                    if guess in word:
                        count = word.count(guess)
                        blanks -= count
                        if blanks == 0:
                            print('You won!')
                            break
                        else:
                            if tries > 0:
                                continue
                            else:
                                print(f'Sorry you lost!... The word was "{word}".')
                    else:
                        if tries > 0:
                            continue
                        else:
                            print(f'Sorry you lost!... The word was "{word}".')
            else:
                tries -= 1
                if guess == word:
                    print('You guessed it right... You won!')
                    break
                else:
                    print('Please enter a character or guess the whole word correctly!')
                continue
    
        user_input = input('Do you want to play again? (y/n): ')
        user_input = user_input.lower()
        if user_input == 'n' or user_input == 'no':
            print('Thanks for playing!')
            break
        elif user_input == 'y' or user_input == 'yes':
            continue
        else:
            print('I take that as a no!')
            break
            

        
if __name__ == '__main__':
    run_game()