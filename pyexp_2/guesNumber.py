import random
target_numbers = random.randint(1, 100)
while True:
    inputNumber = int(input("Enter a number: "))
    if inputNumber > target_numbers:
        print("Too high!")
    elif inputNumber < target_numbers:
        print("Too low!")
    else:
        print("Correct1!")
        break


