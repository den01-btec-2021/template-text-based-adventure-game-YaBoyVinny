def main():
    print("welcome to my game!")
    player_name = input(" what is your name ")
    print(" hi " + player_name)
    life_counter = 3
    print(f" you have   {life_counter}   remaining ")
    print("you can do in 1 of 4 directions, North, East, South, West")
    player_Direction = input("which direction would you like to go in?")
    if player_Direction == "North":
        print("you went North")
    elif player_Direction == "East":
        print("you went East")
    elif player_Direction == "South":
        print("you went South")
    elif player_Direction == "West":
        print("you went West")
    else:
        print("sorry not recognised")


main()