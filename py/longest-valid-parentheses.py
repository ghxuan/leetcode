def longest_valid_parentheses(s):
    """
    :type s: str
    :rtype: int
    """
    stack, left_most, max_length = [], -1, 0
    for idx, i in enumerate(s):
        if i == "(":
            stack.append(idx)
        else:
            if stack:
                stack.pop()
                if stack:
                    max_length = max(max_length, idx - stack[-1])
                else:
                    max_length = max(max_length, idx - left_most)
            else:
                left_most = idx
    return max_length


print(longest_valid_parentheses("(()"))
print(longest_valid_parentheses(")()())"))

# 2
# 4