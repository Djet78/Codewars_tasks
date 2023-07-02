"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the
lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not
consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for
string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the
maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if
this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear
with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing
order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits -
more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".


Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
"""
from collections import Counter


def get_items(s, s_num):
    """
    Extract lowercase letters and their counts form string

    Returned values contain only letter which counts > 1
    :param s: string
    :param s_num: number of entered string.(for further processing)
    :return: list of tuples: [(str('letter' + 's_num'), int(letter counts), ], or empty list

    >>> get_items("my&friend&Paul has heavy hats! &", 1)
    [('y1', 2), ('e1', 2), ('a1', 4), ('h1', 3), ('s1', 2)]

    >>> get_items("codewars", 2)
    []

    >>> get_items("yes, they are here", 2)
    [('y2', 2), ('e2', 5), ('h2', 2), ('r2', 2)]
    """
    s = Counter((x for x in s if x.islower()))
    return [("{}{}".format(k, s_num), v) for k, v in s.items() if v > 1]


def mix(s1, s2):
    # Extract all valid values from both strings
    all_items = get_items(s1, 1) + get_items(s2, 2)

    # Sort items in alphabetical order
    all_items.sort(key=lambda item: item[0][0])

    # Sort list by letters counts in decreasing order
    all_items.sort(key=lambda item: item[1], reverse=True)

    used_values = dict()
    result = []
    for char, count in all_items:
        letter = char[0]
        used = letter in used_values
        if not used:
            result.append("{}:{}".format(char[1], letter * count))
            used_values[letter] = count
        elif used and count == used_values[letter]:
            result[-1] = "=:{}".format(letter * count)

    # Make this sorts in order to build correct string
    result.sort(key=lambda item: item[0][0])  # This sort puts all strings with the '=' symbol to the end
    result.sort(key=len, reverse=True)
    return "/".join(result)


# ---------- Codewars ---------------
def mix2(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1 + c2):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))
