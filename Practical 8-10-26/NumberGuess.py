import random

n = int(input("Enter your guess: "))
comp_guess = random.randrange(1,10)
if n == comp_guess:
    print("Number guessed Correctly!")
    print("Reward granted")
else:
    print("Wrong number!")
    print(comp_guess)