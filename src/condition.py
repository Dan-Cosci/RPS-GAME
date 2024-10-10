from assets import text_banner

values = {
   "r":0,
   "p":1,
   "s":2
}

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
    
def win_check(char_input):
    if char_input == 'p':
        print(text_banner.player_wins)
    if char_input == 'c':
        print(text_banner.comp_wins)
    if char_input == 't':
        print(text_banner.tie)