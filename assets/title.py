"""
This is the title screen of the game so that
it looks somewhat presentable with the CLI
and yes I know this is a bit overkill
"""



# the list of images used for graphic
game_images_right = ['''    ROCK
    _______
___/   ____)
      (_____)
      (_____)
      (____)
---\\__(___)
''','''     PAPER
    _______
___/   ____)____
          ______)
           ______)
          ______)
----\\_________)
''','''     SCISSORS
    _______
___/   ____)____
          ______)
        _________)
        (____)
----\\___(___)
'''
]

combinations_rock = ['''    ROCK                    ROCK
    _______            _______
___/   ____)          (____   \\___
      (_____)        (_____)
      (_____)        (_____)
      (____)          (____)
---\\__(___)            (___)__/---
''',
'''    ROCK                    PAPER
    _______                 _______
___/   ____)           ____(____   \\___
      (_____)        (______
      (_____)        (______
      (____)          (______
---\\__(___)            (__________/---
''',
'''    ROCK                    SCISSORS
    _______                 _______
___/   ____)           ____(____   \\___
      (_____)         (______
      (_____)        (______
      (____)             (____)
---\\__(___)               (___)___/----
'''
]
combinations_paper = ['''    PAPER                   ROCK
    _______              _______
___/   ____)____       (____    \\___
          ______)     (_____)
           ______)    (_____)
          ______)      (____)
----\\_________)         (___)__/---
''',
'''    PAPER                   PAPER
    _______               _______
___/   ____)____     ____(____   \\___
          ______)   (______
           ______)  (______
          ______)    (______
----\\_________)       (__________/---
''',
'''    PAPER                   SCISSORS
    _______               _______
___/   ____)____     ____(____   \\___
          ______)   (______
           ______)  (_____
          ______)      (____)
----\\_________)         (___)___/----
'''
]

combinations_scissors = ['''    SCISSORS                ROCK
    _______               _______
___/   ____)____         (____   \\___
          ______)       (_____)
        _________)      (_____)
        (____)           (____)
----\\___(___)             (___)__/---
''',
'''    SCISSORS                PAPER
    _______               _______
___/   ____)____     ____(____   \\___
          ______)   (______
        _________)  (______
        (____)       (______
----\\___(___)         (__________/---
''',
'''    SCISSORS              SCISSORS
    _______               _______
___/   ____)____     ____(____   \\___
          ______)   (______
        _________)  (_________
        (____)         (____)
----\\___(___)           (___)___/----
'''
]



image_long = f"""   ROCK                PAPER               SCISSORS
    _______            _______             _______    
___/   ____)      ___/    ____)____    ___/   ____)____
      (_____)                ______)             ______)    
      (_____)                 ______)          _________)   
      (____)                 ______)          (____)      
---\\__(___)      ----\\_________)      ----\\___(___) 

"""

# title screen print text
title_screen = f"""
    _______         |
___/   ____)        |               WELCOME TO ROCK PAPER SCISSORS GAME!
      (_____)       |               
      (_____)       |       This game is a recreation by DAN-SCI during the
      (____)        |   5th week of colleg and classes were suspended because of a 
---\\__(___)         |   stupid storm. So he decided to create a CLI game and this is
                    |   the output of that bullshit.
    _______         |
___/   ____)____    |       Rock Paper Scissors is a popular game that is taught to
          ______)   |   children at a young age. One of the very first games that we
           ______)  |   learned about albeit in school or at home. This is a heavily
          ______)   |   designed version of that game that incorporates random CLI and
----\\_________)     |   ASCII art to make this kind of interface
                    |
    _______         |                               RULES
___/   ____)____    |                       * ROCK -> SCISSORS
          ______)   |                       * SCISSORS -> PAPER
        _________)  |                       * PAPER -> ROCK
        (____)      |       this game is just a random practice by DAN so please
----\\___(___)       |   don't take this rendition seriously and say some stupid things
                    |   to the creator.
"""


instru_game = f"""                  INSTRUCTIONS:
        choose from the choices provide
                    r - rock
                    p - paper
                    s - scissors
"""


def main_test():
    print(title_screen)
    for i in range (3):
        print(game_images_left[i])
        print(game_images_right[i])
    print(instru_game)

if __name__ == "__main__":
    main_test()
