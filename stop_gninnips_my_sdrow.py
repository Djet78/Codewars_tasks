def spin_words(sentence):
    """
    Spin five of more letter word in given text.

    Takes in a string of one or more words, and returns the same string,
    but with all five or more letter words reversed.
    Strings passed in will consist of only letters and spaces.
    Spaces will be included only when more than one word is present.
    :return: 'str'. Modified sentence.

    >>> spin_words("Hey fellow warriors")
    'Hey wollef sroirraw'

    >>> spin_words("Short and long words")
    'trohS and long sdrow'
    """
    sentence = sentence.split()
    for idx, word in enumerate(sentence):
        if len(word) >= 5:
            sentence[idx] = word[::-1]
    return " ".join(sentence)


print(spin_words("Short and long words"))
