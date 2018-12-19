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
    def remove_nth_from_end(head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        cur = head
        # cur 比 temp 先行 n 次
        for _ in range(n):
            cur = cur.next
        while cur.next:
            cur = cur.next
            temp = temp.next
        temp.next = temp.next.next
        return head


s = Solution()
start = link_list([1, 2, 3, 4, 5])
show_link(start)
end = s.remove_nth_from_end(start, 2)
show_link(end)
# [1, 2, 3, 4, 5]
# [1, 2, 3, 5]