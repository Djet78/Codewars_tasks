from collections import Counter


def find_it(seq):
    """
    Given an array, find the int that appears an odd number of times.

    There will always be only one integer that appears an odd number of times.

    >>> find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
    5

    >>> find_it([2, 2, 2, 2, 1])
    1

    >>> find_it([1, 1, 2, 2, 2, 2, 1])
    1

    >>> find_it([42])
    42
    """
    for k, v in Counter(seq).items():
        if v % 2 != 0:
            return k


# ------------- Codewars -----------------
from operator import xor
from functools import reduce


def find_it2(xs):
    return reduce(xor, xs)
