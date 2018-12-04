def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    n_ = str(n)
    len_ = len(n_)
    # 分析一下：
    # 可以将 1 分为 个位1、十位1、千位1 ··· ···
    # 假设数为 qwert
    # 那么
    # 个位1 为 qwer × 1 + (1 if t>=1 else 0)
    # 十位1 为 qwe × 10 + (10 if r>1 else 0) + (t+1 if r==1 else 0)
    # 千位1 为 qw × 100 + (100 if e>1 else 0) + (rt+1 if e==1 else 0)
    # ··· ···
    # 最后， 倒序 ：从 高位 到 低位 求和，和就是结果
    # n_[:i] if n_[:i] else 0
    # 是因为 n_[:i] 有可能为 '' 即空字符串，而且 int('') 会报错
    return sum(
        [(int(n_[:i] if n_[:i] else 0) + (1 if j > '1' else 0)) * 10 ** (len_ - i - 1) +
         ((int(n_[i + 1:] if n_[i + 1:] else 0) + 1) if j == '1' else 0)
         for i, j in enumerate(str(n_))])


z = 0
for k in range(3001):
    z += str(k).count('1')
    print(countDigitOne(k), z, k)