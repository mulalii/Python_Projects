import random
import sys

def guessing_game():
    #generate random number 
    maximum = input('Enter your number for max ')

    #Check if number is a digit
    if maximum.isdigit():
        maximum = int(maximum)
    else:
        print('Please enter a number')
        quit()

    rand_num = random.randint(0, maximum)
    count = 0
    
    #Loop to keep playing until we reach False 
    while True:
        if count < 4:
            user_guess = input('Enter a number')
            if user_guess.isdigit():
                user_guess = int(user_guess)
            
            else:
                sys.exit(0)

            if user_guess == rand_num:
                print('You have got it')
                break

            else:
                print('Nope! That ain\'t it')

            count += 1

        #check if user wants to keep playing
        else:
            answer = input('Restart?')
            if answer == 'No':
                print("Leaving the game")
                sys.exit(0) #import sys module

            elif answer == 'Yes':
                print("Staring new game")
                guessing_game()

            else:
                break

guessing_game()