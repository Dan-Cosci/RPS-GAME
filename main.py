from assets import title
from src import player_move, computer_logic, condition

values = {
   "r":0,
   "p":1,
   "s":2
}

def game():
    print(title.title_screen)

    
    move = player_move.p_move()
    com = computer_logic.com_move()
    
    char = condition.checker(move,com)
    print(char)

game()