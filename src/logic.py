"""
game logic for the RPS game to lazy to put the code inside 
the regualr game so ganna make this separate modules for the game
"""

# initialized values of choices
values = {
   "r":0,
   "p":1,
   "s":2
}

# test for the program not a main program
def main_test():
    test_1 = checker("r","r")
    assert test_1 == "t"

    test_2 = checker("r","s")
    assert test_2 == "p"

    test_3 = checker("p","r")
    assert test_3 == "p"
    
    print(test_1,test_2,test_3)


# the main logic of the program
def checker(input_1, input_2):
    
    # checks if input is in the list of values
    if (input_1 or input_2) not in values.keys():
        print("input invalid")
        return ValueError
    
    # main if statement who wins or lose
    if input_1 == input_2:
        return "t"
    if (values[input_1] - values[input_2]) % 3 == 1 :
        return "p"
    else:
        return "c"
        

if __name__=="__main__":
    main_test()
