"""Tests for the dictionary functions."""

__author__ = "730526509"

from dictionary import invert, favorite_color, count


# test invert
def invert_use() -> None:
    """A use case test for invert."""
    nums: dict[str, str] = {'x': 'c', 'y': 'b', 'z': 'a'}
    assert invert(nums) == {'c': 'x', 'b': 'y', 'a': 'z'}


def invert_use_two() -> None:
    """A use case test for invert."""
    num: dict[str, str] = {'apple': 'cat'}
    assert invert(num) == {'cat': 'apple'}


# test favorite_color
def favorite_color_use() -> None:
    """A use case test for favorite_color."""
    nums: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(nums) == "blue"


# test count
def count_use() -> None:
    """A use case test for count."""
    nums: list[str] = ['P', 'y', 't', 'h', 'o', 'n']
    assert count(nums) == {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

  
