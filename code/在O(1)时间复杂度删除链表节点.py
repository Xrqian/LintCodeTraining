"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
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
    @param: node: the node in the list should be deletedt
    @return: nothing
    """

    def deleteNode(self, node):
        # write your code here
        if not node.next:
            node = node.next
        else:
            node.val = node.next.val
            node.next = node.next.next


"""
给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。
eg:
    Linked list is 1->2->3->4, and given node 3, delete the node in place 1->2->4

分析：
    删除函数给的参数是 待删除的节点（只需要把该节点下一个节点前移，删除下一个节点即可）
"""
