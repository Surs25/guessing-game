import random 
def GuessGame():
    num=random.randint(1 ,100)
    Attempts=0 
    while True:
         i=int(input("Guess a number between 1 and 100:"))
         Attempts+=1
         if i<num:
            print ("Too low")
         elif i>num:
            print ("Too high")
         else:
            print (" you guessed the number")
            print("it took you", Attempts, "to guess")
            break 
GuessGame()