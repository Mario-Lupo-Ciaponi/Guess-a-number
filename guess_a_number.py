import random

print("Hello! In this game you have to guess the number from 1-10. When you guess it we will print you the number of"
      "tries.\nNote: This is a beta and new features will be added later on.")

random_number = random.randint(0, 10)

number = int(input("Guess the number: "))
tries = 1
while random_number != number:
    if number > random_number:
        print("Too high!")
    else:
        print("Too low!")

    number = int(input("Guess the number: "))
    tries += 1

print(f"Well done! The number is {random_number}\nTries: {tries}")
