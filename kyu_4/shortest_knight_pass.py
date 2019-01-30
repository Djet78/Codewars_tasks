def generate_empty_board(x, y, init_value):
    return [[init_value for _ in range(x)] for _ in range(y)]


def cell2indexes(cell):
    """
    Transforms chess cell to appropriate list indexes

    :param cell: (str) | Chess cell coordinate i.e. 'h8', 'a1', 'b6', ...
    :return: (tuple(int, int)) | List indexes for given cell

    >>> cell2indexes('a1')
    (7, 0)

    >>> cell2indexes('h1')
    (7, 7)

    >>> cell2indexes('h8')
    (0, 7)

    >>> cell2indexes('e4')
    (4, 4)
    """
    x = -int(cell[1]) % 8
    y = ord(cell[0]) - 97
    return x, y


def knight(p1, p2):
    """
    BFS (breadth-first search) algorithm for finding least number of moves from p1 to p2


    Given two different positions on a chess board, find the least number of moves it would take a knight to get from
    one to the other. The positions will be passed as two arguments in algebraic notation. For example,
    knight("a3", "b5") should return 1.
        The knight is not allowed to move off the board. The board is 8x8.
        For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29
        For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

    :param p1: (str) | Start position
    :param p2: (str) | Target position
    :return:   (int) | Minimal amount of steps to reach destination cell

    >>> knight('a1', 'c1')
    2

    >>> knight('a1', 'f1')
    3

    >>> knight('a1', 'f7')
    5

    >>> knight('f7', 'a1')
    5

    >>> knight('b3', 'f7')
    4

    >>> knight('b5', 'a3')
    1
    """
    if p1 == p2:
        return 0

    # Create board and place start and target cells
    board = generate_empty_board(8, 8, 0)
    start_x, start_y = cell2indexes(p1)
    target_x, target_y = cell2indexes(p2)
    board[start_x][start_y] = 's'
    board[target_x][target_y] = 't'

    POSSIBLE_MOVES = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
    step = 0
    coordinates = [(start_x, start_y)]

    while coordinates:
        step += 1
        next_coordinates = []

        for curr_x, curr_y in coordinates:
            for x, y in POSSIBLE_MOVES:
                x = curr_x + x
                y = curr_y + y

                # Prevents IndexError and reverse indexing
                if not 0 <= x <= 7 or not 0 <= y <= 7:
                    continue

                if not board[x][y]:
                    board[x][y] = step
                    next_coordinates.append((x, y))
                elif board[x][y] == 't':
                    return step

        coordinates = next_coordinates


# ---------- Codewars ---------------
def knight_(p1, p2):
    a, b = [('abcdefgh'.index(p[0]), int(p[1])) for p in [p1, p2]]
    x, y = sorted((abs(a[0] - b[0]), abs(a[1] - b[1])))[::-1]

    if (x, y) == (1, 0): return 3
    if (x, y) == (2, 2) or ((x, y) == (1, 1) and any(p in ['a1', 'h1', 'a8', 'h8'] for p in [p1, p2])): return 4

    delta = x - y

    return delta - 2 * ((delta - y) // (3 if y > delta else 4))
