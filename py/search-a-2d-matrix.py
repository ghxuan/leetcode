class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        left, right = 0, m
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return True
        left, right, cur = 0, n, right
        while left <= right:
            mid = (left + right) // 2
            # quotient, remainder 商 余
            if matrix[cur][mid] < target:
                left = mid + 1
            elif matrix[cur][mid] > target:
                right = mid - 1
            else:
                return True
        return False
