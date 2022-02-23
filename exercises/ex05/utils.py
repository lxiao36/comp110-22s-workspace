"""Some 'list' Utility Functions."""

__author__ = "730526509"


def only_evens(nums: list[int]) -> list[int]:
    x: list[int] = list()
    for num in nums:
        if num % 2 == 0:
            x.append(num)
    return x 


def sub(a_lists: list[int], start: int, end: int) -> list[int]:
    x: list[int] = list()
    while start != end:
        x.append(a_lists[start])
        start += 1
    return x


def concat(first: list[int], second: list[int]) -> list[int]:
    dex = len(second)
    i = 0
    while i != dex:
        first.append(second[i])
        i += 1 
    return first

    
        