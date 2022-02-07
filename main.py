import random
from logo import logo
numbers = list(range(1,101))
print(logo)
print('''Welcome to Number Guessing Game!
I'm thinking of a number between 1 and 100.
''')
ans = random.choice(numbers)

#testing code
# print(f"orei answeru is.. {ans}")

choice = input("Choose a difficulty level. Type 'easy or 'hard': ")

def easy():
    life=10
    while life>0:
        print(f"You have {life} attempts to guess the number.")
        guess=int(input("Make a guess: "))
        if guess == ans:
            print(f"You got it! The number is {ans}")
            break
        else:
            if guess > ans:
                print("Too high")
            else:
                print("Too low")
            life -= 1
            if life == 0:
                print("You've ran out of lives, you lose.")

def hard():
    life=5
    while life>0:
        print(f"You have {life} attempts to guess the number.")
        guess=int(input("Make a guess: "))
        if guess == ans:
            print(f"You got it! The number is {ans}")
            break
        else:
            if guess > ans:
                print("Too high")
            else:
                print("Too low")
            life -= 1
            if life == 0:
                print("You've ran out of lives, you lose.")

if choice == 'easy':
    easy()
elif choice == 'hard':
    hard()
else:
    print("Invalid Input")