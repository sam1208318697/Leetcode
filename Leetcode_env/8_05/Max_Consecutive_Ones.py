# 485. 最大连续1的个数

# 给定一个二进制数组， 计算其中最大连续1的个数。

# 示例 1:
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

# 注意：
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        times = []
        time = 0
        for i in nums:

            if i == 1:
                time = time + 1
            else:
                times.append(time)
                time = 0
        times.append(time)
        return max(times)

sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))