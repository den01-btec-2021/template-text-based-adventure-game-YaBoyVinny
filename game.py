from posixpath import normpath


def main():

    while True:

        print("welcome to my game!")
        player_name = input(" what is your name ")
        print(" hi " + player_name)
        life_counter = 3

        Backpack = [] 

        print(f" you have   {life_counter}   remaining ")
        print("you can go in 1 of 4 directions, North, East, South, West")
        
        while True:
            
            player_Direction = input("which direction would you like to go in?")

            if player_Direction == "North":
                print("you went North")
                # i am trying to fail in puzzle, lose life
                PuzzleGuessNorth = input("what is 10+10")
                if PuzzleGuessNorth == "20":
                    print("correct")
                    Backpack.append("key 1")  # <--- this is how the key is stored in the backpack
            
                else:
                    print("incorrect")
                    life_counter -= 1
                    print(f"you have lost a life, you now have  {life_counter}  remaining ")

                    

            elif player_Direction == "East":
                print("you went East")
                # repeat of the code above
                PuzzleGuessEast = input("what was the name of the man that made the tesla coil ")
                if PuzzleGuessEast == "Nikola tesla":
                    print("correct")
                    Backpack.append("key 2")
                
                else:
                    print("incorrect")
                    life_counter -= 1
                    print(f"you have lost a life, you now have {life_counter} remianing")


            elif player_Direction == "South":
                print("you went South")
                # repeat of North
                print("A: going to the pub, B: getting food, C: getting girls or D: all of the above")
                PuzzleGuessSouth = input("what is Kian Smith known for?")
                if PuzzleGuessSouth == "all of the above":
                    print("correct")
                    Backpack.append("key 3")

                else:
                    print("incorrect")
                    life_counter -= 1
                    print(f"you have lost a life, you now have {life_counter} remaining") 
            
            elif player_Direction == "West":
                print("you went West")
                #
                PuzzlegameWest = input("was this a good game")
                if PuzzlegameWest == "No":
                    print("thank you for your honesty")
                    Backpack.append("key 4")
                else:
                    print("your lying")
            
            else:
                print("sorry not recognised")

            if ("key 1" in Backpack) and ("key 2" in Backpack) and ("key 3" in Backpack) and ("key 4" in Backpack):
                print("door open! Win game!")


            if life_counter == 0:
                print("you have died, try again") 
                break
        exit()
            
main()