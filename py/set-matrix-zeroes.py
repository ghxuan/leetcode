class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 设置一个列表  O(mn)
        # 设置两个列表  O(m+n)
        # 将第一行列 作为储存空间
        m, n, col, row = len(matrix), len(matrix[0]), False, False
        # 检测第一行列
        for i in range(m):
            if matrix[i][0] == 0:
                col = True
                break
        for i in range(n):
            if matrix[0][i] == 0:
                row = True
                break
        # 检测除第一行列外
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 归0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if col:
            for i in range(m):
                matrix[i][0] = 0
        if row:
            for i in range(n):
                matrix[0][i] = 0
        
        
