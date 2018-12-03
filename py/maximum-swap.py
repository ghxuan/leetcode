
def maximumSwap(num):
    """
    :type num: int
    :rtype: int
    """
    num_list = [int(i) for i in str(num)]
    num_sort = sorted(num_list, reverse=True)
    temp = len(num_list) - 1
    num_reverse = num_list[::-1]
    for i, _ in enumerate(num_list):
        if num_list[i] < num_sort[i]:
            num_list[temp - num_reverse.index(num_sort[i])] = num_list[i]
            num_list[i] = num_sort[i]
            return int(''.join([str(i) for i in num_list]))
    return num


print(maximumSwap(2334))
print(maximumSwap(3333))
print(maximumSwap(3233))
print(maximumSwap(32122123))
print(maximumSwap(32122143))
print(maximumSwap(4233332))
print(maximumSwap(4233334))
# 4332
# 3333
# 3332
# 33122122
# 42122133
# 4333322
# 4433332
