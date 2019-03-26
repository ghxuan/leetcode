def combination_sum2(candidates, target):
    res = []
    candidates.sort()

    def dfs(remain, temp, start):
        if not remain:
            res.append(temp[:])
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                n = candidates[i]
                dfs(remain - n, temp + [n], i + 1)

    dfs(target, [], 0)
    return res


print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
# [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]