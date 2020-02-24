# 面试题03.数组中重复的数字
#
# 找出数组中重复的数字。在一个长度为n的数组nums里的所有数字都在0～n - 1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
# 请找出数组中任意一个重复的数字。
#
# 示例1：
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2或3
#
# 限制：
# 2 <= n <= 100000



class Solution:
    def findRepeatNumber(self, nums) -> int:
        res = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                res = nums[i]
                break
        return res