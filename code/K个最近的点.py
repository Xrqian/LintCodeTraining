"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        # write your code here
        self.origin = origin
        return sorted(points, key=self.swap)[:k]

    def swap(self, list_item):
        import math
        x, y = list_item.x, list_item.y
        origin_x, origin_y = self.origin.x, self.origin.y
        return pow(x - origin_x, 2) + pow(y - origin_y, 2), x, y


"""
给定一些 points 和一个 origin，从 points 中找到 k 个离 origin 最近的点。
按照距离由小到大返回。如果两个点有相同距离，则按照x值来排序；若x值也相同，就再按照y值排序
eg:
    points = [[4,6],[4,7],[4,4],[2,5],[1,1]]
    origin = [0, 0]
    k = 3
return
    [[1,1],[2,5],[4,4]]
"""
points = [[4, 6], [4, 7], [4, 4], [2, 5], [1, 1]]
origin = [0, 0]
k = 3
s = Solution()
print(s.kClosest(points, origin, k))
