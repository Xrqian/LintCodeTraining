class Solution:
    """
    @param: n: the nth
    @return: the nth sequence
    """

    def countAndSay(self, n):
        # write your code here
        if n < 1:
            return -1
        elif n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            target_str = "11"
            for x in range(2, n):
                prev_ch = target_str[0]
                same_num = 1
                new_str = ""
                for ch in target_str[1:]:
                    if prev_ch == ch:
                        same_num += 1
                    else:
                        new_str += str(same_num)
                        new_str += prev_ch
                        same_num = 1
                        prev_ch = ch
                new_str += str(same_num)
                new_str += prev_ch
                target_str = new_str
            return target_str


"""
报数指的是，按照其中的整数的顺序进行报数，然后得到下一个数。如下所示：
1, 11, 21, 1211, 111221, ...
1 读作 "one 1" -> 11.
11 读作 "two 1s" -> 21.
21 读作 "one 2, then one 1" -> 1211.
给定一个整数 n, 返回 第 n 个顺序。
给定 n = 5, 返回 "111221".

分析：
    依次往后读， 连续的数字的个数 + 数字
    1       1           -> 11
    2       11          -> 21
    3       21          -> 12 11
    4       1211        -> 11 12 21
    5       111221      -> 31 22 11
    6       312211      -> 13 11 22 21
    7       13112221    -> 11 13 21 32 11
"""
s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
print(s.countAndSay(6))
print(s.countAndSay(7))
