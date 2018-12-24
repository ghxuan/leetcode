# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def link_list(lis):
    """
    :param lis: list
    :return: ListNode
    """
    last_ = None
    for i in lis[::-1]:
        temp = last_
        last_ = ListNode(i)
        last_.next = temp
    return last_


def show_link(node):
    """
    :param node: ListNode
    :return: None
    """
    temp = node
    res = []
    while temp.next:
        res.append(temp.val)
        temp = temp.next
    else:
        res.append(temp.val)
    print(res)


class Solution:
    @staticmethod
    def merge_k_lists(lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        temp = []
        for list_ in lists:
            while list_ is not None:
                temp.append(list_.val)
                list_ = list_.next
        temp.sort()
        res = ListNode(0)
        cur = res
        for i in range(len(temp)):
            cur.next = ListNode(temp[i])
            cur = cur.next
        return res.next


s = Solution()
start1 = link_list([1, 4, 5])
start2 = link_list([1, 3, 4])
start3 = link_list([2, 6])
print('[')
show_link(start1)
show_link(start2)
show_link(start3)
print(']')
start = [start1, start2, start3]
end = s.merge_k_lists(start)
show_link(end)
# [
# [1, 4, 5]
# [1, 3, 4]
# [2, 6]
# ]
# [1, 1, 2, 3, 4, 4, 5, 6]