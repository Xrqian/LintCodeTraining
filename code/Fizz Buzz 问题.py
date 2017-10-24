class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        res = []
        for i in range(1, n + 1):
            if not i % 3 and not i % 5:
                res.append("fizz buzz")
            elif not i % 3:
                res.append("fizz")
            elif not i % 5:
                res.append("buzz")
            else:
                res.append(str(i))
        return res


"""
给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：
如果这个数被3整除，打印fizz.
如果这个数被5整除，打印buzz.
如果这个数能同时被3和5整除，打印fizz buzz.

比如 n = 15, 返回一个字符串数组：

[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]
"""
s = Solution()
print(s.fizzBuzz(15))
