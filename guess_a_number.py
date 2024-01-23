import random

print("Hello! In this game you have to guess the number from 1-10. When you guess it we will print you the number of"
      "tries.\nNote: This is a beta and new features will be added later on.")

print()
print("=============================================================================================================")

print("Do you want your tries to be limited? (Yes/No)")


cap_of_tries = 0
limited_tries_game_mode = False
while True:
    answer = input()

    if answer == "Yes":
        print("Limited tries gamemode activated.")
        limited_tries_game_mode = True
    elif answer == "No":
        print("Normal gamemode activated.")
    else:
        print("Invalid answer. Please type again.")
        continue

    break
print()

print("Please chose a difficulty:")
print("1. Easy(random number in range from 1-10) \n2. Normal(random number in range from 1-100)\n"
      "3. Hard(random number from 1-1000) \n4. Very hard(random number from 1-10000)\n"
      "5. Extreme(random number from 1-100000) \n6. Impossible(random word from 1-1000000)")
print()

random_number = 0

difficulty_in_string = ""
while True:
    difficulty = int(input("Please chose the number of the difficulty that you would like to play: "))

    if difficulty == 1:
        random_number = random.randint(0, 10)
        difficulty_in_string = "Easy"

        if limited_tries_game_mode:
            cap_of_tries = 5
    elif difficulty == 2:
        random_number = random.randint(1, 100)
        difficulty_in_string = "Normal"

        if limited_tries_game_mode:
            cap_of_tries = 15
    elif difficulty == 3:
        random_number = random.randint(1, 1000)
        difficulty_in_string = "Hard"

        if limited_tries_game_mode:
            cap_of_tries = 20
    elif difficulty == 4:
        random_number = random.randint(1, 10000)
        difficulty_in_string = "Very hard"

        if limited_tries_game_mode:
            cap_of_tries = 30
    elif difficulty == 5:
        random_number = random.randint(1, 100000)
        difficulty_in_string = "Extreme"

        if limited_tries_game_mode:
            cap_of_tries = 40
    elif difficulty == 6:
        random_number = random.randint(1, 1000000)
        difficulty_in_string = "Impossible"

        if limited_tries_game_mode:
            cap_of_tries = 50
    else:
        print("Invalid difficulty. Please type again:")
        continue

    break

print("=============================================================================================================")
print()

print(f'You chose "{difficulty_in_string}"')
if limited_tries_game_mode:
    print(f"Cap of tries: {cap_of_tries}")

number = int(input("Guess the number: "))
tries = 1

failed = False

while random_number != number:
    if number > random_number:
        print("Too high!")
    else:
        print("Too low!")

    if limited_tries_game_mode:
        if cap_of_tries < tries:
            failed = True
            break

    number = int(input("Guess the number: "))
    tries += 1

print("=============================================================================================================")
print()

if not failed:
    print(f"Well done! The number is {random_number}!\nTries: {tries}")
else:
    print(print("Out of tries! Better luck next time :)"))
print()

print("Developers high score:\n"
      "Easy: 1 try\n"
      "Normal: 5 tries\n"
      "Hard: 22 tries\n"
      "Very hard: 32 tries")
