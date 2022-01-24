"""EX01 - Chardle - A cute step towards Wordle. """

__author__ = "730526509"

guess: str = str(input("Enter a 5-character word: "))

if len(guess) == 5:
    letter = input("Enter a single character: ")
    if letter in guess and len(letter) < 2:
        print("Searching for " + letter + " in " + guess)
        
        index = 0
        if guess[index] == letter:
            print(letter + " found at index", index)
        if letter in guess:
            index = 1
            if guess[index] == letter:
                print(letter + " found at index", index)
            if letter in guess:
                index = 2
                if guess[index] == letter:
                    print(letter + " found at index", index)
            if letter in guess:
                index = 3
                if guess[index] == letter:
                    print(letter + " found at index", index)
                if letter in guess:
                    index = 4
                    if guess[index] == letter:
                        print(letter + " found at index", index)
            
        
        print(guess.count(letter), "instances of " + letter + " found in " + guess)
    else:
        if len(letter) != 1:
            print("Error: Character must be a single character")
        if len(letter) == 1:
            print("Searching for " + letter + " in " + guess)
            print("No instance of " + letter + " found in " + guess)
    
else:
    print("Error: Word must contain 5 characters")




 
 


    