class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        num_length = len(nums)
        start_pos, end_pos = 0, num_length - 1
        res = []
        while start_pos <= end_pos:
            index = int((start_pos + end_pos) / 2)
            if index > num_length - 1 or index < 0:
                return -1
            elif target > nums[index]:
                start_pos = index + 1
            elif target < nums[index]:
                end_pos = index - 1
            else:
                res.append(index)
                end_pos = index - 1
        return res[-1] if res else -1


"""
给定一个排序的整数数组（升序）和一个要查找的整数target，
用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。
"""
nums = [4, 5, 9, 9, 12, 13, 14, 15, 15, 18]
target = 10
s = Solution()
print(s.binarySearch(nums, target))
