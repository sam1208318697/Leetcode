# 594. 最长和谐子序列
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
# 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

# 示例 1:
# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3]

# 说明: 输入的数组长度最大不超过20,000

class Solution:

    # 遍历法，超时
    def findLHS(self, nums) -> int:
        maxLength = 0
        nums.sort()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                cur = nums[i:j + 1]
                if max(cur) - min(cur) == 1:
                    if len(cur) > maxLength:
                        maxLength = len(cur)

        return maxLength

    # 字典法
    def findLHS2(self, nums) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        res = 0
        for i in dict:
            if i + 1 in dict:
                res = max(res,dict[i]+dict[i+1])
        return res

sol = Solution()
print(sol.findLHS2([1,2,2,2,2,4,4,4,5,5,5,8,8,9]))

















