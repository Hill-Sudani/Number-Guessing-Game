import random

print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess A Number Between 1 To 9")

while chances < 5:
    guess = int(input("Enter Your Guess = "))

    if guess < number:
        print("Your guess was too low: Enter a number heigher than ", guess)

    elif guess > number: 
        print("Your guess was too high: Enter a number lower than ", guess)

    if guess == number:
        print("CONGRATULATIONS YOU WON!")
        break
    chances += 1
    
if not chances < 5:
    print("YOU LOOSE! The number is", number)
    
