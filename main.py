from assets import title
from src import player_move, computer_logic, condition
import os
import time
import sys

values = {
   "r":0,
   "p":1,
   "s":2
}

def game():
    print(title.title_screen)
    play = input("Press <enter> to play and type <q> to quit: ")
    
    if play == 'q':
        sys.exit("thankyouforplaying")
    # time.sleep(2)

    player = choice()

    oppnt = com()
    
    char = condition.checker(player,oppnt)
    print(char)

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
    print("The computer is deciding on the move it should take...")
    
    for i in range(3):
        time.sleep(1)
        print(".", end=" ",flush=True)
    
    print("! ! !")
    time.sleep(1)
    
    
    os.system("cls")
    

    choice = computer_logic.com_move()
    return choice
        

game()