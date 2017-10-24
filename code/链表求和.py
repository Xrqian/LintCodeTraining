"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeList:
    def __init__(self, nums):
        nums.reverse()
        next_node = ListNode(nums[0])
        for num in nums[1:]:
            node = ListNode(num)
            node.next = next_node
            self.head = node
            next_node = node


class Solution:
    """
    @param: l1: the first list
    @param: l2: the second list
    @return: the sum list of l1 and l2
    """

    def addLists(self, l1, l2):
        # write your code here
        head, prev_node, tmp = None, None, 0
        while l1 or l2:
            cal_num = tmp
            cal_num += l1.val if l1 else 0
            cal_num += l2.val if l2 else 0
            cal_num = int(cal_num)
            if not head:
                head = ListNode(cal_num % 10)
                prev_node = head
            else:
                node = ListNode(cal_num % 10)
                prev_node.next = node
                prev_node = node
            tmp = int(cal_num / 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if tmp:
            node = ListNode(tmp % 10)
            prev_node.next = node
        return head


"""
你有两个用链表代表的整数，其中每个节点包含一个数字。
数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
写出一个函数将两个整数相加，用链表形式返回和。
给出两个链表
    3->1->5->null + 5->9->2->null = 8->0->8->null
"""
s = Solution()
l1 = ListNodeList([3, 1, 2])
l2 = ListNodeList([5, 9, 5, 1])
new_head = s.addLists(l1.head, l2.head)
while l1.head:
    print(l1.head.val, end=' -> ')
    l1.head = l1.head.next
print('null')
while l2.head:
    print(l2.head.val, end=' -> ')
    l2.head = l2.head.next
print('null')
while new_head:
    print(new_head.val, end=' -> ')
    new_head = new_head.next
print('null')
