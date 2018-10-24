def prime_word(array):
    """
    X and Y are playing a game. A list will be provided which contains n pairs of strings and integers. They have to
    add the integeri to the ASCII values of the stringi characters. Then they have to check if any of the new added
    numbers is prime or not. If for any character of the word the added number is prime then the word will be
    considered as prime word.

    Can you help X and Y to find the prime words?

    Example:
    prime_word([["Emma", 30], ["Liam", 30]])  ->  [1, 1]
    For the first word "Emma" ASCII values are: 69 109 109 97
    After adding 30 the values will be: 99 139 139 127
    As 139 is prime number so "Emma" is a Prime Word.
    """
    res = []
    for name, num in array:
        res.append(0)
        for code in set(name.encode("ascii")):
            if is_prime(code + num):
                res[-1] = 1
                break
    return res


def is_prime(num):
    for div in range(3, (num // 2) + 1):
        if num % div == 0:
            return False
    return True


# --------- Codewars ----------
def is_prime2(n):
    return n == 2 or n > 2 and n % 2 and all(n % x for x in range(3, int(n ** .5 + 1), 2))


def prime_word2(array):
    return [any(is_prime2(ord(c) + n) for c in name) for name, n in array]
