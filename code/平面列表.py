class Solution(object):
    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if not hasattr(self, 'res_list'):
            self.res_list = []
        if isinstance(nestedList, list):
            for item in nestedList:
                if isinstance(item, list):
                    self.flatten(item)
                else:
                    self.res_list.append(item)
            return self.res_list
        else:
            return [nestedList]


"""
给定一个列表，该列表中的每个要素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表。
(如果给定的列表中的要素本身也是一个列表，那么它也可以包含列表。)
样例
给定 [1,2,[1,2]]，返回 [1,2,1,2]。
给定 [4,[3,[2,[1]]]]，返回 [4,3,2,1]。
"""
nestedList = 10
s = Solution()
print(s.flatten(nestedList))
