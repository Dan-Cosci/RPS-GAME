"""
this is a program that enables the player
to move and allow the player a given action
"""

values = {
   "r":0,
   "p":1,
   "s":2
}

# the function that is gonna be used
def p_move():
    
    # initializing the list of correct choices
    choice = list(values.keys())
    
    # basic error handling if the user did not give correct input
    while True:
        try:
            player_choice = input("your pick: ")
            
            # error management
            if player_choice not in choice:
                print("your choice is invalid")
                raise ValueError
        except:
            pass
        else:
            break
    
    # returns player's choice
    return player_choice


# test if the function is running correctly
def main_test():
    test = p_move()
    print(test)

if __name__ == "__main__":
    main_test()
