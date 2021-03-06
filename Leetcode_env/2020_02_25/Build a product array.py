# 面试题66.构建乘积数组
#
# 给定一个数组
# A[0, 1,…, n - 1]，请构建一个数组
# B[0, 1,…, n - 1]，其中
# B中的元素B[i] = A[0]×A[1]×…×A[i - 1]×A[i + 1]×…×A[n - 1]。不能使用除法。
#
# 示例:
# 输入: [1, 2, 3, 4, 5]
# 输出: [120, 60, 40, 30, 24]
#
# 提示：
# 所有元素乘积之和不会溢出32位整数
# a.length <= 100000

class Solution:
    def constructArr(self, a):
        res = [1 for i in range(len(a))]
        left = 1
        for i in range(len(res)):
            res[i] = left
            left *= a[i]

        right = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= right
            right *= a[i]

        return res

