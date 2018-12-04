def spiralMatrixIII(R, C, r0, c0):
    """
    :type R: int
    :type C: int
    :type r0: int
    :type c0: int
    :rtype: List[List[int]]
    """
    if not (0 <= r0 < R and 0 <= c0 < C):
        return 0
    res = [[r0, c0]]
    if R * C == 1:
        return res
    # k 表示每个边的长度
    for k in range(1, 2 * (R + C), 2):
        # 左、下、右、上 (四个方向移动)
        for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k + 1), (-1, 0, k + 1)):
            print(dr, dc, dk)
            for _ in range(dk):
                r0 += dr
                c0 += dc
                # 判断是否出界
                if 0 <= r0 < R and 0 <= c0 < C:
                    # 添加路径
                    res.append([r0, c0])
                    if len(res) == R * C:
                        return res