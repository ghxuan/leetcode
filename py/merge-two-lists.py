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
    def merge_two_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l2.next, l1)
            return l2


s = Solution()
start1 = link_list([1, 2, 4])
start2 = link_list([1, 3, 4])
show_link(start1)
show_link(start2)
end = s.merge_two_lists(start1, start2)
show_link(end)
# [1, 2, 4]
# [1, 3, 4]
# [1, 1, 2, 3, 4, 4]