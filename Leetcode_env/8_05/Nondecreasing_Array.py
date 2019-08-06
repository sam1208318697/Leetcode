# 665. 非递减数列
# 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

# 示例 1:
# 输入: [4,2,3]
# 输出: True
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

# 示例 2:
# 输入: [4,2,1]
# 输出: False
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 说明:  n 的范围为 [1, 10,000]。

class Solution:
    def checkPossibility(self, nums) -> bool:
        if len(nums) <= 1:
            return True
        # count为已经修改的次数
        count = 0
        # 遍历列表找到第一个不符合条件的数并进行修改
        for i in range(len(nums)-1):
            # 只修改第一个出现的不符合条件的数字
            if count == 1:
                break
            # 不符合条件的情况
            if nums[i] > nums[i+1]:
                count = count + 1
                # 判断不符合条件的数字是否为列表第一个数
                if i > 0:
                    # 如果不是，则需要依据前后数字来决定，具体修改哪里的数
                    # 如果前一个数也大于后一个数，则说明i-1位置上的数字必然等于i位置，则需要修改第i+1位置上的数
                    if nums[i-1]> nums[i+1]:
                        nums[i+1] = nums[i]
                    else:
                        # 如果前一个数字小于等于后一个数，则将前一个数的值复制给当前的i位置的数
                        nums[i] = nums[i-1]
                else:
                    # 如果是第一个数出现问题，则将第二个数的值复制给第一个数，使其相等
                    nums[i] = nums[i+1]
        # 如果遍历后发现count值为0，则说明列表有序，并未曾有修改过，则直接返回True
        if count == 0:
            return True

        print(nums)
        # 再遍历修改后的列表，如还遇到不符合条件的情况则返回False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False

        return True







sol = Solution()
print(sol.checkPossibility([2,3,5,5,1]))