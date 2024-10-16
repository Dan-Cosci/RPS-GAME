from assets import title, text_banner
from src import player_move, computer_logic, condition
import os
import time
import sys

import functools
print = functools.partial(print, flush=True)

values = {
   "r":0,
   "p":1,
   "s":2
}

def round():
    print(title.title_screen)
    play = input("Press <enter> to play and type <q> to quit: ")
    
    if play == 'q':
        sys.exit("thankyouforplaying")
    
    player = 0
    computer = 0

    rounds = get_int("how may rounds would you like to play?: ")
    for round in range(rounds):
        winner = game()
        time.sleep(2)
        if winner == 'p':
            player += 1
        elif winner == 'c':
            computer += 1
        else:
            continue

    if player > computer:
        print(text_banner.win_text)
    elif player < computer:
        print(text_banner.lose_text)
    else:
        print(text_banner.tie)           


def game():
    
    # time.sleep(2)

    player = choice()

    oppnt = com()
    time.sleep(2)
    os.system("cls")
    
    char = condition.checker(player,oppnt)
    face_off(player, oppnt)
    condition.win_check(char)
    return char

def choice():
    while True:
        try:
            os.system("cls")
            print(title.instru_game)
            print(title.image_long)
            move = player_move.p_move()
            print("You have choosen: ")
            print(title.game_images_right[values[move]])
            response = input("Are you sure with your choice <y/n>: ")
            if response.lower() == 'n':
                raise ValueError   
        except:
            pass
        else:
            return move

def com():
    os.system("cls")    
    for j in range(3):
        print("The computer is deciding on the move it should take...")
        for i in range(3):
            time.sleep(0.5)
            print(".", end=" ")
        time.sleep(0.5)
        os.system("cls")    
        
    os.system("cls")
    print("THE COMPUTER HAS DECIDED!")
    time.sleep(2)
    print("The computer has chosen:")
    time.sleep(1)
    choice = computer_logic.com_move()
    print(title.game_images_right[values[choice]])
    return choice

def face_off(player,com):
    if player == 'r':
        print(title.combinations_rock[values[com]])
    if player == 'p':
        print(title.combinations_paper[values[com]])
    if player == 's':
        print(title.combinations_scissors[values[com]])

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass
        else:
            break

round()