"""Example of an function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon, ["Kanye West", "Pete David"]))
# Define a function named contains
# Two parameters:
# 1. needle - the strogn we're searching for
# 2. haystack - the list we're searching through 


def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm:
    #   For each item in the haystack
    #       Test if it is equal to the needle
    #           if so, return True
    for item in haystack:
        if item == haystack:
            return True
    # After testing all items, return false, becasue not found
    # Returns true if needle in haystack, false otherwise
    return False