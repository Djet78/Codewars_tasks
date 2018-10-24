def encrypt(text, n):
    """
    Take every 2nd char from the string, then the other chars, that are not every 2nd char,
    and concat them as new String.Do this n times!

    Examples:
    "This is a test!", 1 -> "hsi  etTi sats!"
    "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"


    If the input-string is null or empty return exactly this value!
    If n is <= 0 then return the input text.

    :param text: any 'str'
    :param n: permutation counter
    :return: 'str'. encrypted text
    """
    if n <= 0:
        return text
    for _ in range(n):
        even_letters = []
        odd_letters = []
        for idx, char in enumerate(text):
            if idx % 2 == 0:
                even_letters.append(char)
            else:
                odd_letters.append(char)
        text = "".join(odd_letters) + "".join(even_letters)
    return text


def decrypt(encrypted_text, n):
    """
    Decrypt encrypted text

    :param encrypted_text: any 'str'
    :param n: permutation counter
    :return: 'str'. decrypted text
    """
    if n <= 0:
        return encrypted_text
    for _ in range(n):
        decrypted = []
        odd_letters = encrypted_text[:len(encrypted_text) // 2]
        even_letters = encrypted_text[len(encrypted_text) // 2:]
        try:
            for idx in range(len(even_letters)):
                decrypted.append(even_letters[idx])
                decrypted.append(odd_letters[idx])
        except IndexError:
            pass
        encrypted_text = "".join(decrypted)
    return encrypted_text


# ____________\\ Codewars //____________


# 1)
def codewars_decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def codewars_encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


# 2)
def codewars_decrypt2(s, n):
    if not s: return s
    o, l = len(s) // 2, list(s)
    for _ in range(n):
        l[1::2], l[::2] = l[:o], l[o:]
    return ''.join(l)


def codewars_encrypt2(s, n):
    if not s: return s
    for _ in range(n):
        s = s[1::2] + s[::2]
    return s
