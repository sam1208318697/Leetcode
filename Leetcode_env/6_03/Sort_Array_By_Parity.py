# 905. 按奇偶排序数组
# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
# 你可以返回满足此条件的任何数组作为答案。

# 示例：
# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

class Solution:
    def sortArrayByParity(self, A):

        res = []
        for i in range(len(A)):
            if A[i]%2!=0:
                res.append(A[i])
            else:
                res.insert(0,A[i])
        return res




sol = Solution()
print(sol.sortArrayByParity([3,1,2,4]))


