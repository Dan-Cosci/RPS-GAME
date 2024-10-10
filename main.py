from assets import title
from src import player_move, computer_logic, condition
import os
import time

values = {
   "r":0,
   "p":1,
   "s":2
}

def game_intro():
    print(title.title_screen)
    time.sleep(2)
    os.system("cls")
    print(title.instru_game)
    print(title.image_long)

    move = player_move.p_move()
    com = computer_logic.com_move()
    
    char = condition.checker(move,com)
    print(char)

game_intro()