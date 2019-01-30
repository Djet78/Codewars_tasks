from operator import mul
from itertools import accumulate


def persistence(n):
    """
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
    which is the number of times you must multiply the digits in num until you reach a single digit.

    For example:
    persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                    # and 4 has only one digit

    persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                     # 1*2*6=12, and finally 1*2=2

    persistence(4) # returns 0, because 4 is already a one-digit number
    """
    iterations = 0
    while len(str(n)) != 1:
        iterations += 1
        n = (int(x) for x in str(n))  # create generator of numbers
        n = list(accumulate(n, mul))[-1]  # multiply all numbers and take the result
    return iterations


# -------- Codewars ------------
from functools import reduce


def persistence_(n):
    i = 0
    while n >= 10:
        n = reduce(mul, [int(x) for x in str(n)])
        i += 1
    return i
