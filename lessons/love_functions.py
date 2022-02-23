"""Given a name as a parameter, reuturns a loving string."""


def love(name: str) -> str:
    """Given a name as a parameter, reuturns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1 
    return love_note

x
def mystery(n: int) -> str:
    """A useless function."""
    i: int = 0 
    while i < n: 
        if i % 2 == 1:
            return "ohh"
        i += 1 
    return "ahh"
