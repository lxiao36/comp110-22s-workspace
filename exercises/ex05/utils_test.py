"""Tests for the utils functions."""

__author__ = "730526509"

from utils import only_evens, sub, concat


# test only_even
def test_only_evens_edge() -> None:
    """A edge case test for only_even."""
    nums: list[int] = []
    assert only_evens(nums) == []


def test_only_evens_use() -> None:
    """A use case test for only_even."""
    nums: list[int] = [1, 2, 3]
    assert only_evens(nums) == [2]


def test_only_evens_use_two() -> None:
    """A second use case test for only_even."""
    nums: list[int] = [1, 2, 3, 4]
    assert only_evens(nums) == [2, 4]


# test sub
def test_sub_edge_() -> None:
    """A edge case test for sub."""
    a_list: list[int] = []
    assert sub(a_list, 0, 0) == []


def test_sub_use() -> None:
    """A use case test for sub."""
    a_list: list[int] = [-1, 0, 1, 2]
    assert sub(a_list, 1, 5) == [0, 1, 2]


def test_sub_use_two() -> None:
    """A second use case test for sub."""
    a_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a_list, 1, 5) == [2, 3, 4, 5]


# test concat
def test_concat_edge() -> None:
    """A edge case test for concat."""
    first: list[int] = [0]
    second: list[int] = [0]
    assert concat(first, second) == [0, 0]


def test_concat_use() -> None:
    """A use case test for concat."""
    first: list[int] = [11, 22, 22, 11]
    second: list[int] = [22, 11, 11, 22]
    assert concat(first, second) == [11, 22, 22, 11, 22, 11, 11, 22]


def test_concat_use_two() -> None:
    """A second use case test for concat."""
    first: list[int] = [1, 2, 3, 4]
    second: list[int] = [1, 2, 3, 4]
    assert concat(first, second) == [1, 2, 3, 4, 1, 2, 3, 4]