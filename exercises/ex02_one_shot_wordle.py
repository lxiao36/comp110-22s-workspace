"""EX02 - making Wordle."""

__author__ = "730526509"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = str("python")
guess: str = str(input("What is your 6-letter guess? "))
anwser = 0  


while anwser == 0:
    if len(guess) != 6:
        guess = input("That was not 6 letters! Try again: ")
    elif len(guess) == 6 and guess != secret:
        index = 0
        ONE = "a"
        TWO = "b" 
        THREE = "c"
        FOUR = "d" 
        FIVE = "e"
        SIX = "f"
      
        if guess[index] == secret[index]:
            ONE = GREEN_BOX
        elif guess[index] != secret[index] and guess[index] in secret:
            ONE = YELLOW_BOX
        elif guess[index] != secret[index]:
            ONE = WHITE_BOX
            
        index = 1
        if guess[index] == secret[index]:
            TWO = GREEN_BOX
        elif guess[index] != secret[index] and guess[index] in secret:
            TWO = YELLOW_BOX
        elif guess[index] != secret[index]:
            TWO = WHITE_BOX
        
        index = 2
        if guess[index] == secret[index]:
            THREE = GREEN_BOX
        elif guess[index] != secret[index] and guess[index] in secret:
            THREE = YELLOW_BOX
        elif guess[index] != secret[index]:
            THREE = WHITE_BOX
        
        index = 3
        if guess[index] == secret[index]:
            FOUR = GREEN_BOX
        elif guess[index] != secret[index] and guess[index] in secret:
            FOUR = YELLOW_BOX
        elif guess[index] != secret[index]:
            FOUR = WHITE_BOX

        index = 4
        if guess[index] == secret[index]:
            FIVE = GREEN_BOX
        elif guess[index] != secret[index] and guess[index] in secret:
            FIVE = YELLOW_BOX
        elif guess[index] != secret[index]:
            FIVE = WHITE_BOX

        index = 5
        if guess[index] == secret[index]:
            SIX = GREEN_BOX
        elif guess[index] != secret[index] and guess[index] in secret:
            SIX = YELLOW_BOX
        elif guess[index] != secret[index]:
            SIX = WHITE_BOX
        
        print(f"{ONE}{TWO}{THREE}{FOUR}{FIVE}{SIX}")
        print("Not quite. Play again soon!")
        anwser = 1
    
    elif len(guess) == 6 and guess == secret:
        anwser = 1
        print(f"{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}")
        print("Woo! You got it!")