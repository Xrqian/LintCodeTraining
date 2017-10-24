class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        if n < 1:
            return -1
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b, res = 0, 1, 0
            for x in range(n - 2):
                res = a + b
                a = b
                b = res
            return res
