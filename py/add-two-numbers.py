# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        # 第一次对 next_ 的修改
        # 其实只是对 res 的修改
        next_, temp = res, 0
        while True:
            n1, l1 = (l1.val, l1.next) if l1 else (0, None)
            n2, l2 = (l2.val, l2.next) if l2 else (0, None)
            temp, next_.val = divmod(n1 + n2 + temp, 10)
            if l1 or l2 or temp:
                next_.next = ListNode(0)
                next_ = next_.next
            else:
                next_.next = None
                return res


def init(s):
    last = None
    for i in s:
        node = ListNode(int(i))
        node.next = last
        last = node
    return last


# j = init('342')
# print(j.val, j.next.val, j.next.next.val)
# 2 4 3


sol = Solution()
a = sol.add_two_numbers(init('342'), init('465'))
print(a.val, a.next.val, a.next.next.val)
a = sol.add_two_numbers(init('1348'), init('468'))
print(a.val, a.next.val, a.next.next.val, a.next.next.next.val)
# 7 0 8
# 6 1 8 1