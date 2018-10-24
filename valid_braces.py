def is_valid_braces(string):
    """
    Function takes a string of braces, and determines if the order of the braces is valid.

    A string of braces is considered valid if all braces are matched with the correct brace.
    :param string: only consist of parentheses, brackets and curly braces: '()[]{}'.
    Return false if string consists not only '()[]{}'
    :return: True if valid, or False otherwise
    """
    close_bracers = [")", "]", "}"]
    open_bracers = ["(", "[", "{"]
    if not string or string[0] in close_bracers or string[-1] in open_bracers:
        return False
    parentheses = {")": "(", "}": "{", "]": "["}
    check = []
    for char in string:
        if char in open_bracers:
            check.append(char)
        else:
            if not check or check.pop() != parentheses[char]:
                return False
    return not check
