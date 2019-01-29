def divisors(integer):
    """
    Looks for all divisors of given integer(except for 1 and integer itself)

    :param integer: any positive 'int' value
    :return: list of increasing divisors or if integer is prime number return string: "{} is prime".format(integer)

    >>> divisors(50)
    [2, 5, 10, 25]

    >>> divisors(233)
    '233 is prime'

    >>> divisors(288)
    [2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 32, 36, 48, 72, 96, 144]
    """
    if type(integer) is not int or integer <= 2:
        raise ValueError("Only numbers bigger than 2 allowed!")
    divisors_lst = []
    for i in range(2, int(integer/2) + 1):
        if integer % i == 0:
            divisors_lst.append(i)
    if not divisors_lst:
        return "{} is prime".format(integer)
    return divisors_lst
