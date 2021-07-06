import random
import math

class guess_number:
    
    def start_guess(self):
        # input lower bound
        print("Hello! Welcome to guess the number!")
        lb = int(input("Enter lower bound:"))
        # input upper bound
        ub = int(input("Enter upper bound:"))
        # generate random number between range
        num = random.randint(lb, ub)
        print("\n\t You have", round(math.log(ub - lb + 1, 2)),"chances to guess the integer!\n")
        # create counter for number of guesses
        count = 0
        
        # minimum number of guesses depends on range
        while count < math.log(ub - lb + 1, 2):
            count += 1
            try:
                 # user input guessed number
                guess = int(input("Guess a number (Integers only): "))
                if int(guess) < lb or int(guess) > ub:
                    raise ValueError("Please guess a number within the given range")
                # if condition is met then user wins and loop breaks
                if guess == num:
                    print("Congratulations! You won")
                    playAgain = input("Would you like to play again? (Enter Yes/No) ")
                    count = 0
                    num = int(random.randint(lb, ub))
                    if playAgain.lower() == "no":
                        print("Exiting...")
                        break
                # if incorrect guess then loop continuous
                elif guess > num:
                    print("The guessed number is too high. Retry!")
                elif guess< num:
                    print("Tthe guessed number is too low. Retry!")
                       
            except ValueError:
                print("That was not a valid number.  Try again...")
        
        # if user runs out of guesses the following is displayed
        if count >= math.log(ub - lb + 1, 2):
            print("\n The number is %d" % num)
            print("\t Game Over!")
            
    