"""
This is the title screen of the game so that
it looks somewhat presentable with the CLI
and yes I know this is a bit overkill
"""

# initializes piglet font used for victory or defeats
import pyfiglet


# the list of images used for graphic
game_images = ['''
    _______
___/   ____)
      (_____)
      (_____)
      (____)
---\__(___)
''','''
    _______
___/   ____)____
          ______)
           ______)
          ______)
----\_________)
''','''
    _______
___/   ____)____
          ______)
        _________)
        (____)
----\___(___)
'''
]


# title screen print text
title_screen = f"""
    _______         |
___/   ____)        |               WELCOME TO ROCK PAPER SCISSORS GAME!
      (_____)       |               
      (_____)       |       This game is a recreation by DAN-SCI during the
      (____)        |   5th week of colleg and classes were suspended because of a 
---\__(___)         |   stupid storm. So he decided to create a CLI game and this is
                    |   the output of that bullshit.
    _______         |
___/   ____)____    |       Rock Paper Scissors is a popular game that is taught to
          ______)   |   children at a young age. One of the very first games that we
           ______)  |   learned about albeit in school or at home. This is a heavily
          ______)   |   designed version of that game that incorporates random CLI and
----\_________)     |   ASCII art to make this kind of interface
                    |
    _______         |                               RULES
___/   ____)____    |                       * ROCK -> SCISSORS
          ______)   |                       * SCISSORS -> PAPER
        _________)  |                       * PAPER -> ROCK
        (____)      |       this game is just a random practive my DAN so please
----\___(___)       |   don't take this rendition seriously and say some stupid things
                    |   to the creatlor.
"""


player_wins = pyfiglet.figlet_format("Player wins the round!")
comp_wins = pyfiglet.figlet_format("Computer wins the round!")

win_text = pyfiglet.figlet_format("YOU WIN!")
lose_text = pyfiglet.figlet_format("YOU LOST YOU SUCK")

instru_game = f"""

                INSTRUCTIONS:
        choose from the choices provide
                    r - rock
                    p - paper
                    s - scissors
"""


def main_test():
    print(title_screen)
    for i in range (3):
        print(game_images[i])
    print(player_wins)
    print(comp_wins)
    print(instru_game)


    print(win_text, lose_text)

if __name__ == "__main__":
    main_test()
