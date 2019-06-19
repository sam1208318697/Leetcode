# 53. 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 进阶:
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。



class Solution:
    # 动态规划
    # dp[i] 表示以 nums[i] 结尾的连续子数组的最大和。
    # 接下来分类讨论就变得容易多了，因为 dp[i - 1] 一定以 nums[i-1] 结尾，那么 dp[i] 就可以有两种情况：
    # 1、把 nums[i] 直接接在 dp[i - 1] 表示的那个数组的后面；例如：dp[i - 1] = 3，nums[i] = 5，接在后面，当然越接越大。
    # 2、单独的一个 nums[i]。这种情况也比较好想到，比如：dp[i - 1] = -3，nums[i] = 5，加上前面的数反而我越来越小了，干脆“另起炉灶”吧。
    # 以上两种情况的最大值就是 dp[i] 的值。最后不要忘记，最终的结果应该是把所有的 dp[0]、dp[1]、……、dp[n - 1] 都看一遍，取最大值。
    # 总结：
    # 1、定义状态：dp[i] 表示以 nums[i] 结尾的连续子数组的最大和。
    # 2、状态转移方程：dp[i] = max(num[i], dp[i - 1] + num[i])。

    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0

        if len(nums)==1:
            return nums[0]

        ans = [0 for _ in range(len(nums))]

        ans[0] = nums[0]
        for i in range(1,len(nums)):
            ans[i] = max(ans[i-1]+nums[i],nums[i])

        return max(ans)






sol = Solution()
print(sol.maxSubArray([-2,1,-3,4]))