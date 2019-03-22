def solve_sudo_ku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    cases = dict()
    t = set('123456789')
    rows = [t.copy() for _ in range(9)]
    cols = [t.copy() for _ in range(9)]
    blocks = [t.copy() for _ in range(9)]

    for l in range(9):
        for c in range(9):
            s = (c // 3) + 3 * (l // 3)
            v = board[l][c]
            if v == ".":
                cases[(l, c)] = s
            else:
                rows[l].remove(v)
                cols[c].remove(v)
                blocks[s].remove(v)

    def solve():
        if not cases:
            return True
        min_len = 9
        for (i, j), b in cases.items():
            num = len(rows[i] & cols[j] & blocks[b])
            if num < min_len:
                min_len = num
                x, y = i, j

        if min_len == 0:
            return False

        b = cases.pop((x, y))
        nums = rows[x] & cols[y] & blocks[b]
        for m in nums:
            rows[x].remove(m)
            cols[y].remove(m)
            blocks[b].remove(m)
            if solve():
                board[x][y] = m
                return True
            rows[x].add(m)
            cols[y].add(m)
            blocks[b].add(m)
        cases[(x, y)] = b
        return False

    solve()
    print(board)


solve_sudo_ku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])

# [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
#  ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
#  ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
#  ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
#  ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
#  ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
#  ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
#  ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
#  ['3', '4', '5', '2', '8', '6', '1', '7', '9']]