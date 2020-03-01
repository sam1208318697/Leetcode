# 386. 字典序排数
# 给定一个整数 n, 返回从 1 到 n 的字典顺序。

# 例如，
# 给定 n =13，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。
# 请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。


class Solution:
    def lexicalOrder(self, n: int):
        res = []
        for i in range(1,n+1):
            res.append(str(i))
        res.sort()
        for i in range(len(res)):
            res[i] = int(res[i])

        return res



sol = Solution()
print(sol.lexicalOrder(13))