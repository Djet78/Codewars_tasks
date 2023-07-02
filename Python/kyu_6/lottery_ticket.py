def bingo(ticket, win):
    """
    Time to win the lottery!

    Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the
    jackpot. Example ticket:

    [ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
    To do this, you must first count the 'mini-wins' on your ticket. Each sub array has both a string
    and a number within it. If the character code of any of the characters in the string matches the number, you get a
    mini win. Note you can only have one mini win per sub array.

    Once you have counted all of your mini wins, compare that number to the other input provided (win). If your total
    is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

    All inputs will be in the correct format. Strings on tickets are not always the same length.
    """
    mini_wins = 0
    for chars, code in ticket:
        for char in chars:
            if ord(char) == code:
                mini_wins += 1
                break
    return 'Winner!' if mini_wins >= win else 'Loser!'


# -------- Codewars ------------
def bingo2(ticket, win):
    return 'Winner!' if sum(chr(n) in s for s, n in ticket) >= win else 'Loser!'
