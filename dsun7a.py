#Dawei Sun
#CTC389
#9-9-2026

my_number = 3

guess = int(input("Guess: "))

while guess >= 1 and guess <= 5 and guess != 3:
    guess = int(input("Try again: "))

if guess == 3:
    print("You win!")
elif guess > 3:
    print("You lost. My number is lower.")
else:
    print("You lost. My number is higher.")

