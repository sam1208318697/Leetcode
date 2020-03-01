# 922.按奇偶排序数组 II

# 给定一个非负整数数组A， A中一半整数是奇数，一半整数是偶数。
# 对数组进行排序，以便当A[i]为奇数时，i也是奇数；当A[i]为偶数时， i也是偶数。
# 你可以返回任何满足上述条件的数组作为答案。

# 示例：
# 输入：[4, 2, 5, 7]
# 输出：[4, 5, 2, 7]
# 解释：[4, 7, 2, 5]，[2, 5, 4, 7]，[2, 7, 4, 5]也会被接受。

# 提示：
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

class Solution:
    def sortArrayByParityII(self, A):
        l1 = []  # 存放奇数
        l2 = []  # 存放偶数
        for i in A:
            if i % 2 == 0:
                l2.append(i)
            else:
                l1.append(i)
        res = []
        i = 0
        while i < len(A):
            if i % 2 == 0:
                res.append(l2.pop())
                i = i + 1
            else:
                res.append(l1.pop())
                i = i + 1

        return res

sol = Solution()
print(sol.sortArrayByParityII([4, 2, 5, 7]))