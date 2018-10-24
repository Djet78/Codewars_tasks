def rgb(r, g, b):
    """
    The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a
    hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument
    values that fall out of that range should be rounded to the closest valid value.

    The following are examples of expected output values:

    rgb(255, 255, 255) # returns FFFFFF
    rgb(255, 255, 300) # returns FFFFFF
    rgb(0,0,0) # returns 000000
    rgb(148, 0, 211) # returns 9400D3
    """
    lst = [r, g, b]
    for idx in range(3):
        if lst[idx] > 255:
            lst[idx] = 255
        elif lst[idx] < 0:
            lst[idx] = 0
    return "{:02X}{:02X}{:02X}".format(*lst)


#  -----------------  Codewars --------------
def rgb2(r, g, b):
    round_ = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round_(r), round_(g), round_(b))


def rgb3(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args))
