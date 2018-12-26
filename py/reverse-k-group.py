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
    def reverse_k_group(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 递归， 每次循环 k 次
        # 假如 长度小于 k 不反转
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next
        # 反转前 k 个节点
        new = self.reverser(head, cur)
        head.next = self.reverse_k_group(cur, k)
        return new

    @staticmethod
    def reverser(first, last):
        """
        :param first: ListNode
        :param last: ListNode
        :return: ListNode
        """
        pre = last
        while first != last:
            # 第一条和第四条 将 first 更新
            t = first.next
            # 将 后面的所有内容 放到 第一个后面
            first.next = pre
            pre = first
            first = t
        return pre


s = Solution()

start = link_list([1, 2, 3, 4, 5])
show_link(start)
end = s.reverse_k_group(start, 2)
show_link(end)

start = link_list([1, 2, 3, 4, 5])
end = s.reverse_k_group(start, 3)
show_link(end)
# [1, 2, 3, 4, 5]
# [2, 1, 4, 3, 5]
# [3, 2, 1, 4, 5]