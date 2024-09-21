import title


def main():
    print(title.title_screen)
    player = input("What is your name? : ")
    
    print(f"Hello {player}! Welcome to rock paper scissors")
    print(title.instru_game)

if __name__ == "__main__":
    main()

