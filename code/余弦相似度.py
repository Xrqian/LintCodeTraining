class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Cosine similarity
    """

    def cosineSimilarity(self, A, B):
        # write your code here
        import math
        numerator = sum(a * b for a, b in zip(A, B))
        denominator = math.sqrt(sum(a * a for a in A)) * math.sqrt(sum(b * b for b in B))
        return float("%.4f" % ((numerator / denominator) if denominator else 2))


"""
给出 A = [1, 2, 3], B = [2, 3 ,4].
返回 0.9926.
给出 A = [0], B = [0].
返回 2.0000

分析：
    公式
    sum(ai * bi for i in range(a_length))
    -----------------------------------------------
    sqrt(sum(ai * ai for i in range(a_length))) * sqrt(sum(bi * bi for i in range(b_length)))
"""
A, B = [1, 4, 0], [1, 2, 3]
s = Solution()
print(s.cosineSimilarity(A, B))
