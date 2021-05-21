import random

randNumber = random.randint(1,100)
userGuess = -1
guesses = 0

while randNumber != userGuess:
    userGuess = int(input("Enter your guess[1,100] : "))
    guesses +=1
    if userGuess > randNumber:
        print("You guessed it wrong! Enter a smaller number")
    elif userGuess < randNumber:
         print("You guessed it wrong! Enter a larger number")
    else:
        print("You guessed it right!")
print("You take "+str(guesses)+" guesses")
