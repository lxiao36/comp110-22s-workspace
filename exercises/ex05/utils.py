"""Some list Utility Functions."""

__author__ = "730526509"


def only_evens(nums: list[int]) -> list[int]:
    """Insert list then will return even numbers."""
    x: list[int] = list()
    for num in nums:
        if num % 2 == 0:
            x.append(num)
    return x 


def sub(a_lists: list[int], start: int, end: int) -> list[int]:
    """Returns numbers between start and end -1."""
    x: list[int] = list()
    max_length = len(a_lists)
    if start < 0:
        start = 0
    if end > max_length:
        end = max_length
    if max_length == 0 or start > max_length or end <= 0:
        a_lists = list()
    while start != end:
        x.append(a_lists[start])
        start += 1
    return x


def concat(first: list[int], second: list[int]) -> list[int]:
    """Returns two lists put together."""
    dex = len(second)
    i = 0
    while i != dex:
        first.append(second[i])
        i += 1 
    return first