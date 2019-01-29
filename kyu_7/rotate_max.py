from collections import deque


def max_rot(n):
    """
    Take a number: 56789. Rotate left, you get 67895.

    Keep the first digit in place and rotate left the other digits: 68957.

    Keep the first two digits in place and rotate the other ones: 68579.

    Keep the first three digits and rotate left the rest: 68597. Now it is over since keeping the first four it remains
    only one digit which rotated is itself.

    You have the following sequence of numbers:

    56789 -> 67895 -> 68957 -> 68579 -> 68597

    and you must return the greatest: 68957.

    >>> max_rot(56789)
    68957

    >>> max_rot(38458215)
    85821534

    >>> max_rot(1)
    1

    >>> max_rot(10)
    10

    >>> max_rot(121)
    211
    """
    rotations = [n]
    n = str(n)
    head = deque()
    tail = deque(n)
    for _ in range(len(n) - 1):
        tail.rotate(-1)
        head.append(tail.popleft())
        rotations.append(int("".join(head + tail)))
    return max(rotations)


# ------------ Codewars ----------
def max_rot2(n):
    s, arr = str(n), [n]
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]
        arr.append(int(s))
    return max(arr)
