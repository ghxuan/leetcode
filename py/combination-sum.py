def combination_sum(candidates, target):
    res = []
    candidates.sort()

    def backtrack(remain, temp, start):
        if not remain:
            res.append(temp)
        else:
            for i, n in enumerate(candidates[start:]):
                if n > remain:
                    break
                backtrack(remain - n, temp + [n], start + i)

    backtrack(target, [], 0)
    return res


print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([2, 3, 5], 8))
# [[2, 2, 3], [7]]
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]