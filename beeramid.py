def beeramid(bonus, price):
    """
    Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome!
    To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy,
    and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because
    let's pretend it's Friday too.

    A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the
    next, 16, 25...

    Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given
    the parameters of:

    1) your referral bonus, and

    2) the price of a beer can

    For example:

    beeramid(1500, 2); // should === 12
    beeramid(5000, 3); // should === 16
    """
    level = 0
    while True:
        level += 1
        price_for_lvl = price * (level**2)
        if bonus < price_for_lvl:
            level -= 1
            break
        bonus -= price_for_lvl
    return level


# --------------- Codewars ----------------

def beeramid2(bonus, price):
    """
    'O(1) solution thanks to wolframalpha'

    p.s. I don`t know how it works. Awesome
    """
    k = bonus // price
    d = (3 * (11664*k*k - 3) ** .5 + 324 * k) ** (1/3)
    n = (d/3 + 1/d - 1) / 2
    return k > 0 and int(n.real+1e-12)
