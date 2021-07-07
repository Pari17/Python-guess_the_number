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
        print(" You have", round(math.log(ub - lb + 1, 2)),"chances to guess the integer!")
        # create counter for number of guesses
        count = 0
        
        # minimum number of guesses depends on range
        while count < math.log(ub - lb + 1, 2):
            count += 1
            try:
                 # user input guessed number
                guess = int(input("Guess the number (Integers only): "))
                if int(guess) < lb or int(guess) > ub:
                    raise ValueError("Guessed number is out of range. Please try again.")
                # if condition is met then user wins and loop breaks
                if guess == num:
                    print("Congratulations! You won in", count,"guesses")
                    play_again = input("Would you like to replay? (yes/no)")
                    count = 0
                    num = int(random.randint(lb, ub))
                    if play_again.lower() == "no":
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
            print("The number is", num)
            print("\t Game Over!")
            
    