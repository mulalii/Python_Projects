import random
import sys

user_wins = 0
cpu_wins = 0
game_list = ['rock', 'paper', 'scissors']

while True:
    #take the user input and game count
    user_turn = input('Choose (0) rock, (1) paper,(2) scissors or Q to quit: ').lower()

    #check if user input is not rock paper or scissor
    if user_turn == 'q':
        break

    if user_turn not in game_list:
        continue

    random_number = random.randint(0,2)
    computer_turn = game_list[random_number]
    print('computer picked ', computer_turn)

    if user_turn == 'rock' and computer_turn == 'scissors':
        print('you win')
        user_wins += 1
        continue

    elif user_turn == 'paper' and computer_turn == 'rock':
        print('you win')
        user_wins += 1
        continue

    elif user_turn == 'paper' and computer_turn == 'rock':
        print('you win')
        user_wins += 1
        continue

    else:
        print('you lose')
        cpu_wins += 1

    print(f'you won {user_wins}')
    print(f'computer won {cpu_wins}')

    