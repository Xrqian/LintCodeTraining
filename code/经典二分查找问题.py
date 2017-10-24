class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        length = len(nums)
        start_pos, end_pos = 0, length - 1
        if target > nums[end_pos] or target < nums[start_pos]:
            return -1
        while start_pos <= end_pos:
            target_index = int((end_pos + start_pos) / 2)
            if target > nums[target_index]:
                start_pos = target_index + 1
            elif target < nums[target_index]:
                end_pos = target_index - 1
            else:
                return target_index
        return -1
