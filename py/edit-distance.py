class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        result = [{} for _ in range(len(word1) + 1)]

        def getDistance(i, j):
            if i == 0: return j
            if j == 0: return i
            if j in result[i]: return result[i][j]

            if word1[i - 1] == word2[j - 1]:
                distance = getDistance(i - 1, j - 1)
            else:
                distance = min(getDistance(i - 1, j - 1),
                              getDistance(i - 1, j),
                              getDistance(i, j - 1)) + 1
            result[i][j] = distance
            return distance

        return getDistance(len(word1), len(word2))
