# 198. 打家劫舍

# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

# 示例 1:
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。

# 示例 2:
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。

class Solution:

    # 方法1，递归法，超出时间限制
    def rob(self, nums) -> int:

        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0],nums[1])
        if l == 3:
            return max(nums[0]+nums[2],nums[1])
        if l > 2:
            return max( self.rob(nums[0:l-2]) + nums[l-1] , self.rob(nums[0:l-3]) + nums[l-2] )



    # 方法2，动态规划
    # 当前最大的累计收益= max(前一家的收益，前前一家的收益加上当前的收益)
    # dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    def rob2(self, nums) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        p = nums[0]
        q = max(nums[0],nums[1])
        for i in range(2,l):
            next = max(p+nums[i],q)
            p,q = q,next
        return q




sol = Solution()
print(sol.rob2([5,1,1,4]))