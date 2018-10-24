def one_two_three(n):
    """
    There are no explanations. You have to create the code that gives the following results in Python and Ruby:

    one_two_three(0) == [0, 0]
    one_two_three(1) == [1, 1]
    one_two_three(2) == [2, 11]
    one_two_three(3) == [3, 111]
    one_two_three(19) == [991, 1111111111111111111]
    """
    ones = int("1" * n) if n else 0
    digits = ["0", ]
    nines = n // 9
    rest = n - (nines * 9)
    digits.append("9" * nines)
    if rest:
        digits.append(str(rest))
    digits = int("".join(digits))
    return [digits, ones]


# ------ Codewars ---------

def one_two_three2(n):
    return [int('9' * (n / 9) + (str(n % 9) if n % 9 else '') or 0), int(('1'*n) or 0)]
