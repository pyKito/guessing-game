import random

n = random.randrange(1, 11)  # Random number between 1 and 10
counter = 0

while True:
    user_input = input("Write any number from 1 to 10 as numbers only: ")

    try:
        answer = int(user_input)
    except ValueError:
        print("Well, I guessed you will try that too.")
        continue  # Skip to the next loop iteration
    if answer < 1 or answer > 10:
        print("Hey, smartass, I said only from 1 to 10!!!")
        continue  # Invalid number, skip to next input
    counter += 1
    if answer == n:
        print(f"Correct! You guessed the number in {counter} tries.")
        break
    elif answer > n:
        print("The number is lower than the answer")
    else:
        print("The number is bigger than the answer")
    if counter == 3:
        print(f"Too many attempts! The correct number was: {n}")
        break



