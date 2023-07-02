from timeit import timeit

def digital_root(n):
    """
    In this kata, you must create a digital root function.

    A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n.
    If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only
    applicable to the natural numbers.

    Here's how it works (Ruby example given):

    digital_root(16)
    => 1 + 6
    => 7

    digital_root(942)
    => 9 + 4 + 2
    => 15 ...
    => 1 + 5
    => 6

    digital_root(132189)
    => 1 + 3 + 2 + 1 + 8 + 9
    => 24 ...
    => 2 + 4
    => 6
    """
    while n > 9:
        sum_ = 0
        for digit in str(n):
            sum_ += int(digit)
        n = sum_
    return int(n)


# ------------- Codewars --------------
def digital_root2(n):
    return n % 9 or n and 9
