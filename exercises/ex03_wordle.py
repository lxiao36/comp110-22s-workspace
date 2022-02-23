"""The real wordle."""

__author__ = "730526509"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(guess: str, char: str) -> bool:
    """Return letter in word."""
    assert len(char) == 1
    if char in guess:
        return(True)
    else:
        return(False)


def emojified(guess: str, secret: str) -> str:
    """The green, yellow, and white boxes."""
    boxes: str = ""
    index = 0 
    while len(guess) == len(secret) and index != len(guess):
        if guess[index] == secret[index]:
            boxes = boxes + GREEN_BOX
        elif guess[index] != secret[index] and guess[index] in secret:
            boxes = boxes + YELLOW_BOX
        elif guess[index] != secret[index]:
            boxes = boxes + WHITE_BOX
        index = index + 1 
    return boxes


def input_guess(ab: int) -> str:
    """Limits the character in the word."""
    guess = input(f"Enter a {ab} character word: ")
    counter = 1 
    while counter == 1: 
        if len(guess) != ab:
            guess = (input(f"That wasn't {ab} chars! Try again: "))
        else:
            counter == 0
            return(guess)
    return(guess)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    """Can change python in secret to other words."""
    secret: str = str("codes")
    number = 1
    turns = 6
    while turns != 0:
        print(f"=== Turn {number}/6 ===")
        word_length = len(secret)
        y = input_guess(word_length)
        print(emojified(y, secret))
        number = number + 1 
        turns = turns - 1
        if y == secret:
            turns = 0
            print(f"You won in {number - 1}/6 turns!")
        elif turns == 0:
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()