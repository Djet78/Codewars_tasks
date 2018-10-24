from string import ascii_uppercase


def play_pass(text, shift):
    """
    Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently
    they can be guessed due to common cultural references. You can get your passphrases stronger by different means.
    One is the following:

    choose a text in capital letters including or not digits and non alphabetic characters,

    shift each letter by a given number but the transformed letter must be a letter (circular shift),
    replace each digit by its complement to 9,
    keep such as non alphabetic and non digit characters,
    downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
    reverse the whole result.
    #Example:

    your text: "BORN IN 2015!", shift 1

    1 + 2 + 3 -> "CPSO JO 7984!"

    4 "CpSo jO 7984!"

    5 "!4897 Oj oSpC"

    With longer passphrases it's better to have a small and easy program. Would you write it?

    >>> play_pass("BORN IN 2015!", 1)
    '!4897 Oj oSpC'

    >>> play_pass("BORN IN 2015!", 3)
    '!4897 Ql qUrE'

    >>> play_pass("Some random TEXT and number: 223149", 1)
    '058677 :SfCnVo eOb uYfU NpEoBs fNpT'
    """
    letters = ascii_uppercase
    modulo = len(letters)
    pwd = []
    for pos, char in enumerate(text.upper()):
        if char.isalpha():
            idx = letters.index(char)
            char = letters[(idx + shift) % modulo]
            if pos % 2 != 0:
                char = char.lower()
        elif char.isdigit():
            char = str(9 - int(char))
        pwd.append(char)
    return "".join(reversed(pwd))


print(play_pass("Some random TEXT and number: 223149", 1))
