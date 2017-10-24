"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        # write your code here
        node = head
        prev_node, new_head = node, node
        while prev_node:
            if prev_node.val == val:
                node = node.next
                prev_node = node
            else:
                node = node.next
                break
        new_head = prev_node
        while node:
            if node.val == val:
                prev_node.next = node.next
            else:
                prev_node = node
            node = node.next
        return new_head
