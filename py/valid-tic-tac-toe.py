def validTicTacToe(board):
    """
    :type board: List[str]
    :rtype: bool
    """
    string = ''
    for i in board:
        string += i
    len_x = string.count('X')
    len_o = string.count('O')
    if 0 <= len_x - len_o <= 1:
        list_x = [i for i, x in enumerate(string) if x == 'X']
        list_o = [i for i, x in enumerate(string) if x == 'O']
        if not (has_same_str(list_x) and has_same_str(list_o)):
            return True
    return False


def has_same_str(index):
    """
    :param index: List[int]
    :return: bool
    """
    for x in range(3):
        if x in index and x+3 in index and x+6 in index:
            return True
        if x*3 in index and x*3+1 in index and x*3+2 in index:
            return True
    if (0 in index and 4 in index and 8 in index) or (2 in index and 4 in index and 6 in index):
        return True
    else:
        return False


print(validTicTacToe(['O  ', '   ', '   ']))
print(validTicTacToe(['XOX', ' X ', '   ']))
print(validTicTacToe(['XXX', '   ', 'OOO']))
print(validTicTacToe(['XOX', 'O O', 'XOX']))
print(validTicTacToe(['XOX', 'OXO', 'XOX']))

# 结果：
# False
# False
# False
# True
# True