import math


def is_square(n):
    """
    Checks is 'n' a square number

    :param n: 'int' value
    :return: bool value depending on if given number is square number
    """
    if type(n) is not int:
        raise ValueError("Wrong given type, should be integer instead")
    return n > -1 and math.sqrt(n) == int(math.sqrt(n))
