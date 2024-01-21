import random

print("Hello! In this game you have to guess the number from 1-10. When you guess it we will print you the number of"
      "tries.\nNote: This is a beta and new features will be added later on.")

print()
print("=============================================================================================================")

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
    elif difficulty == 2:
        random_number = random.randint(1, 100)
        difficulty_in_string = "Normal"
    elif difficulty == 3:
        random_number = random.randint(1, 1000)
        difficulty_in_string = "Hard"
    elif difficulty == 4:
        random_number = random.randint(1, 10000)
        difficulty_in_string = "Very hard"
    elif difficulty == 5:
        random_number = random.randint(1, 100000)
        difficulty_in_string = "Extreme"
    elif difficulty == 6:
        random_number = random.randint(1, 1000000)
        difficulty_in_string = "Impossible"
    else:
        print("Invalid difficulty. Please type again:")
        continue

    break

print("=============================================================================================================")
print()

print(f'You chose "{difficulty_in_string}"')
number = int(input("Guess the number: "))
tries = 1

while random_number != number:
    if number > random_number:
        print("Too high!")
    else:
        print("Too low!")

    number = int(input("Guess the number: "))
    tries += 1

print("=============================================================================================================")
print()
print(f"Well done! The number is {random_number}!\nTries: {tries}")
