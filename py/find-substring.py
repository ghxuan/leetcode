def find_substring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if not s or not words:
        return []
    lens, len_word, len_subs, times = len(s), len(words[0]), 0, {}
    times = {}
    for word in words:
        len_subs += len_word
        times[word] = times.get(word) + 1 if times.get(word) else 1
    res = []
    for i in range(min(len_word, lens - len_subs + 1)):
        start = i
        cur = {}
        while i + len_subs <= lens:
            temp = start
            start += len_word
            word = s[temp:start]
            if word not in times:
                i = start
                cur.clear()
            else:
                cur[word] = cur.get(word) + 1 if cur.get(word) else 1
                while cur[word] > times[word]:
                    temp = i
                    i += len_word
                    cur[s[temp:i]] -= 1
                if start - i == len_subs:
                    res.append(i)
    return res


print(find_substring('barfoothefoobarman', ["foo", "bar"]))
print(find_substring('wordgoodstudentgoodword', ["word", "student"]))
# [0, 9]
# []