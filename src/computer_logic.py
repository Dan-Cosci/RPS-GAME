"""
this is the basic function of how the
computer moves in the game, this is not
to be taken seriouly if seen so yeah
"""

values = {
   "r":0,
   "p":1,
   "s":2
}

# uses random module as main psuedo AI
import random as r


# test for the computer choices if it works
def main_test():
    for _ in range(10):
        choices = com_move()
        print(choices)

# main function to be use
def com_move():
    choices = list(values.keys())
    return r.choice(choices)


if __name__ == "__main__":
    main_test()
