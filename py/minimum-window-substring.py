class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_, n, hash_map, left, cnt, res = len(s) + 1, len(t), dict(), 0, 0, ""
        for char in t:
            hash_map[char] = hash_map.get(char, 0) + 1
        for i, str_ in enumerate(s):
            if str_ in hash_map.keys():
                if hash_map[str_] > 0:
                    cnt += 1
                hash_map[str_] -= 1
            while cnt == n:
                temp = i - left + 1
                if temp < min_:
                    min_ = temp
                    res = s[left:i + 1]
                if s[left] in hash_map.keys():
                    hash_map[s[left]] += 1
                    if hash_map[s[left]] > 0:
                        cnt -= 1
                left += 1
        return res


ss = Solution()
# print(ss.minWindow('ADOBECODEBANC', 'ABC'))
# print(ss.minWindow('ADOBECODEBANC', 'ABCF'))
print(ss.minWindow('a', 'a'))
