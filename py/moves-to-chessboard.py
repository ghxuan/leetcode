

import random


def movesToChessboard(board):
    """
    :type board: List[list[int]]
    :rtype: int
    """
    # print(board)
    print()
    reversed_board = board.__reversed__()
    rows = len(board)
    for i in range(rows):
        if -1 <= board[i].count(0) - board[i].count(1) <= 1:
            pass
        else:
            return -1
        if -1 <= reversed_board[i].count(0) - reversed_board[i].count(1) <= 1:
            pass
        else:
            return -1
    time = 0
    # 换行
    for i in range(1, rows):
        temp = i
        while board[i][0] == board[i - 1][0]:
            temp += 1
            if temp == rows:
                break
            board[i], board[temp] = board[temp], board[i]
        if temp != i:
            time += 1
    reversed_board = board.__reversed__()
    for i in range(1, rows):
        temp = i
        while board[0][i] == board[0][i - 1]:
            temp += 1
            if temp == rows:
                break
            reversed_board[i], reversed_board[temp] = reversed_board[temp], reversed_board[i]
        if temp != i:
            time += 1
    board = reversed_board.__reversed__()
    print('-' * 10)
    print(time)
    print(board)
    print('-' * 10)
    if check(board):
        return time
    return -1


def check(board):
    """
    :type board: List[list[int]]
    :rtype: bool
    """
    rows = len(board)
    for i in range(1, rows):
        if board[0][i] == board[0][i - 1]:
            return False
        if board[i][0] == board[i - 1][0]:
            return False
    for i in range(1, rows):
        for j in range(1, rows):
            # print((i, j))
            # print('行', (f'[{j}][{i}]', f'[{j-1}][{i}]'))
            # print('列', (f'[{i}][{j}]', f'[{i}][{j-1}]'))
            if board[i][j] == board[i][j - 1]:
                return False
            if board[j][i] == board[j - 1][i]:
                return False
    return True


class List(list):
    def __repr__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self])

    # 行列互换
    def __reversed__(self):
        return List(map(list, zip(*self)))


class Board(object):
    def __init__(self):
        self.rows = random.randrange(2, 32)
        self.board = List([random.randint(0, 1) for _ in range(self.rows)] for _ in range(self.rows))


print(movesToChessboard(Board().board))

# -1

print(movesToChessboard(Board().board))

# -1

print(movesToChessboard(List([[0, 1], [1, 0]])))

# ----------
# 0
# 0 1
# 1 0
# ----------
# 0

print(movesToChessboard(List([[0, 1, 0], [1, 0, 1], [0, 1, 0]])))

# ----------
# 0
# 0 1 0
# 1 0 1
# 0 1 0
# ----------
# 0

print(movesToChessboard(List(
    [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]])))

# ----------
# 2
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
# ----------
# 2

