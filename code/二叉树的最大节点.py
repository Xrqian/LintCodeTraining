class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        # write your code here
        return self.recursion(root)

    def recursion(self, root):
        # 递归方式查询最大的数字
        if root:
            max_list = [root]
            if root.left:
                max_list.append(self.maxNode(root.left))
            if root.right:
                max_list.append(self.maxNode(root.right))
            return max(max_list, key=lambda x: x.val)
        else:
            return None


"""
在二叉树中寻找值最大的节点并返回。
"""
