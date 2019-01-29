def first_dup(s):
    """
    Find the first character that repeats in a String and return that character.

    first_dup('tweet') => 't'
    first_dup('like') => None

    This is not the same as finding the character that repeats first. In that case, an input of 'tweet' would yield 'e'.
    """
    for idx in range(len(s)):
        if s[idx + 1:].find(s[idx]) != -1:
            return s[idx]
    return None


# ------- Codewars ------------
def first_dup2(s):
    return next((x for x in s if s.count(x) > 1), None)
