def catch_sign_change(lst):
    """
    Count how often sign changes in array.

    result
    number from 0 to ... . Empty array returns 0

    example
    const arr = [1, -3, -4, 0, 5]

    | elem | count |
    |------|-------|
    |  1   |  0    |
    | -3   |  1    |
    | -4   |  1    |
    |  0   |  2    |
    |  5   |  2    |

    return 2;
    """
    times = 0
    for idx, el in enumerate(lst[:-1]):
        next_ = lst[idx + 1]
        if next_ < 0 <= el or next_ >= 0 > el:
            times += 1
    return times
