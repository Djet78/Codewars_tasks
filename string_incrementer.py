def increment_string(strng):
    """
    Your job is to write a function which increments a string, to create a new string. If the string already ends
    with a number, the number should be incremented by 1. If the string does not end with a number the number 1
    should be appended to the new string.

    Examples:

    foo -> foo1

    foobar23 -> foobar24

    foo0042 -> foo0043

    foo9 -> foo10

    foo099 -> foo100

    Attention: If the number has leading zeros the amount of digits should be considered.
    """
    if not strng or not strng[-1].isdigit():
        return strng + "1"
    digits = []
    for char in strng[::-1]:
        if not char.isdigit():
            break
        digits.append(char)
    num = "".join(digits[::-1])
    num_len = len(num)
    increment = str(int(num) + 1)
    leading_zeros = num_len - len(increment)
    return strng[:-num_len] + "0"*leading_zeros + increment


# -------- Codewars ---------

def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
