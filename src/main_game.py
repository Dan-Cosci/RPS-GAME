"""
main game loop for the rock paper scissors games
this is the main game function of this god forsaken
mini CLI game
"""

import player_move
import computer_logic
import logic

def main():
    move = input("Choose r p s : ")
    com = computer_logic.com_move()
    
    winner = logic.checker(move, com)

    print (winner)

if __name__ == "__main__":
    main()
