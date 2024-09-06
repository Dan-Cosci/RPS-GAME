"""

this is a recreation of the game rock-paper-scissors in python
this game a PvE because not it's hard to code a program that
requires to player input and you can't seen the other player's input

"""

import random as ran
import time


values = {
    "rock": 0,
    "paper": 1,
    "scissors": 2
}

def main():
    while True:
        print("""
Welcome to rock paper scissors
            """)

        reply = input("<enter> to start, q + <enter to quit> ")
        if reply == "q":
            break
        else:
            main_game()


def main_game():
    player = player_move()
    print(f"you choose {player}")
    print(f"computer's turn!")
    computer = com_move()
    print("the computer has choosen!")
    print(check_winner(player, computer))

def com_move():
    choice = ran.choice(list(values.keys()))
    return values[choice]

def player_move():
    while True: 
        try:
            choice = input("choose: rock, paper, scissors ")
            if choice not in values.keys():
                raise ValueError
        except:
            pass
        else:
            break
    return choice

def check_winner(player, computer):
    inp_1 = values[player]
    
    print(inp_1, computer)

    if inp_1 == computer:
        return "it's a tie"
    if (inp_1 - computer) % 3 == 1:
        return "player win"
    else:
        return "computer wins"

if __name__=="__main__":
    main()
