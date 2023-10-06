#This is a guess the number game test your guessing supremacy 
import random
secret_number=random.randint(1,30)
print("I'm thinking of a number between 1 to 30")
#Ask the player to guess 6 times
try:
  for guessesTaken in range(1,7):
    guess=int(input("Take a guess : "))
    if guess < secret_number:
      print("Your guess is too low")
    elif guess > secret_number:
      print("Your guess is too high")
    else:
      break
  if guess == secret_number:
	  print("Good job!!\n you guessed my number is "+str(guessesTaken)+" guesses")
  else:
    print("Nope.\nThe number I thinking of was "+str(secret_number))
except KeyboardInterrupt:
    print('\n\nYou quit!')
		
