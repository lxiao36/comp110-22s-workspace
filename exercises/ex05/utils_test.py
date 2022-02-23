"""Tests for the utils functions."""

__author__ = "730526509"

from utils import only_evens, sub, concat


# test only_even
def test_only_evens_edge() -> None:
    nums: list[int] = []
    assert only_evens(nums) == []


def test_only_evens_use() -> None:
    nums: list[int] = [1, 2, 3]
    assert only_evens(nums) == [2]


def test_only_evens_use_two() -> None:
    nums: list[int] = [1, 2, 3]
    assert only_evens(nums) == [2]


# test sub
def test_sub_edge_() -> None:
    a_list: list[int] = [40, 40, 40, 40]
    assert sub(a_list, 1, 4) == [40, 40, 40]


def test_sub_use() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_use_two() -> None:
    a_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a_list, 1, 5) == [2, 3, 4, 5]


# test concat
def test_concat_edge() -> None:
    first: list[int] = [0]
    second: list[int] = [0]
    assert concat(first, second) == [0, 0]


def test_concat_use() -> None:
    first: list[int] = [11, 22, 22, 11]
    second: list[int] = [22, 11, 11, 22]
    assert concat(first, second) == [11, 22, 22, 11, 22, 11, 11, 22]


def test_concat_use_two() -> None:
    first: list[int] = [1, 2, 3, 4]
    second: list[int] = [1, 2, 3, 4]
    assert concat(first, second) == [1, 2, 3, 4, 1, 2, 3, 4]