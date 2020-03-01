# 448. 找到所有数组中消失的数字
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

# 示例:
# 输入:[4,3,2,7,8,2,3,1]
# 输出:[5,6]



class Solution:
    # 方法一，超时
    def findDisappearedNumbers(self, nums):
        length = len(nums)
        count = 0
        for i in range(length):
            if nums.count(i+1) == 0 :
                nums.append(i+1)
                count += 1
        nums = nums[len(nums)-count:len(nums)]
        return nums


    # 方法二
    def findDisappearedNumbers2(self, nums):
        return list(set(range(1, len(nums) + 1)) - set(nums))




sol = Solution()
print(sol.findDisappearedNumbers2([4,3,2,7,8,2,3,1]))