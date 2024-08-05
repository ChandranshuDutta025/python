import random

target = random.randint(1,100)

while True:
    guess = int(input("Guess the target: "))
    if (guess==target):
        print("You guessed it right")
        break
    elif guess<target-20:
         print("Your guess is too low")
    elif guess>target+20:
         print("Your guess is too high")
    elif abs(guess - target) < 10:
        if guess < target:
            print("Your guess is close, guess larger")
        else:
            print("Your guess is close, guess smaller")
    elif abs(guess - target) < 5:
        if guess < target:
            print("Your guess is very close, guess larger")
        else:
            print("Your guess is very close, guess smaller")

        

