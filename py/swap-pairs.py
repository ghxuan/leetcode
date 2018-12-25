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
    def swap_pairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        res = head.next
        head.next = self.swap_pairs(res.next)
        res.next = head
        return res


s = Solution()
start = link_list([1, 2, 3, 4])
show_link(start)
end = s.swap_pairs(start)
show_link(end)
# [1, 2, 3, 4]
# [2, 1, 4, 3]