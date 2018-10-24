def narcissistic(value):
    """
    A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of
    digits.

    For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
    The Challenge:

    Your code must return true or false depending upon whether the given number is a Narcissistic number.
    """
    str_val = str(value)
    val_len = len(str_val)
    pow_sum = 0
    for num in str_val:
        pow_sum += int(num)**val_len
    return value == pow_sum


# ------------------ Codewars -------------------


def narcissistic_(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
