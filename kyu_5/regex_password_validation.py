from re import compile, VERBOSE


"""
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number

Valid passwords will only be alphanumeric characters.
"""
# My -----------

regex = compile("""
^                       # Start of word
((?=.*\d)               # at least one number
(?=.*[a-z])             # at least one lowercase letter
(?=.*[A-Z])             # at least one uppercase letter
(?!.*[./ +\\!\-?_]).    # avoided chars
{6,})                   # at least 6 characters long
$                       # End of word
""", VERBOSE)


# ------------ Codewars ---------------


regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)
