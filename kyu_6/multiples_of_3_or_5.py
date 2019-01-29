def solution(number):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    multiples is 23.

    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

    Note: If the number is a multiple of both 3 and 5, only count it once.

    >>> solution(100)
    2318

    >>> solution(10)
    23

    >>> solution(4)
    3

    >>> solution(6)
    8
    """
    return sum((x for x in range(number) if x % 3 == 0 or x % 5 == 0))


# -------- Codewars --------
def solution2(number):
    """ O(1) complexity """
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result