
def main():
    
    print("Welcome to the Game")

    player_name = input("what is your name? ")

    print(f"Hello {player_name}.")

    lives = 3
    print(f"You have {lives} remaining lives.")

    backpack = [] # initialise empty list for backpack

    while True:
      direction = input("Which direction do you want to go? Please choose from North, South, East or West.")    

      if direction == "North":
        room_direction = "North"
        puzzle = "What is 10 + 10? "
        puzzle_solution = "20"
        key_number = "1"
        lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)

      elif direction == "South":
        room_direction = "South"
        puzzle = "What is the name of the man who made the tesla coil? "
        puzzle_solution = "Nikola Tesla"
        key_number = "2"
        lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)

      elif direction == "East":
        room_direction = "East"
        print("A: going to the pub, B: getting food, C: getting girls or D: all of the above")
        puzzle = "What is kian smith know for? "
        puzzle_solution = "all of the above"
        key_number = "3"
        lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
      
      elif direction == "West": 
        room_direction = "West"
        puzzle = "do you think this is a good game "
        puzzle_solution = "no"
        key_number = "4"
        lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)

      else:
        print("Room not recognised!")   

      #if back pack is full, open door and win game.
      if ("Key 1" in backpack) and ("Key 2" in backpack) and ("Key 3" in backpack) and ("Key 4" in backpack):
        print("Win!") 
        exit()

      if lives == 0:
        print("Lose!")
        exit()

def in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number):
  print(f"You entered the {room_direction} Room.")
  puzzle_guess = input(puzzle)
  if puzzle_guess == puzzle_solution:
    print(f"Correct. Key {key_number} collected.")
    if f"Key {key_number}" not in backpack:
     backpack.append(f"Key {key_number}")
    else:
      print("you have already collected that key")
  else:
    lives -= 1
    print(f"Incorrect. You have {lives} lives remaining.")

  return lives

def addition(a,b):
    return a+b

def test_addition():
  assert addition(3,2) == 5
  assert addition(-1,0) == -1
  assert addition(-1,1) == 0

def test_in_room():

    backpack = []
    lives = 3
    room_direction = "north"
    puzzle = "what is 6 + 3?"
    puzzle_solution = "9"
    key_number = "1"
    
    #check incorrect?
    #assert in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number) == 2

    #check correct?
    assert in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number) == 3 #lives =
    assert f"Key {key_number}" in backpack #check that this is key in the backpack
    in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
    assert backpack != ["Key 1", "Key 1"]

if __name__ == '__main__':
  #main()
 #value = addition(3,2)
  #print(value)
  #test_addition()
  test_in_room()