# 169. 求众数
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在众数。

# 示例 1:
# 输入: [3,2,3]
# 输出: 3

# 示例 2:
# 输入: [2,2,1,1,1,2,2]
# 输出: 2

class Solution:
    # 正常思路，会超出时间限制
    def majorityElement(self, nums) -> int:

        majority_element = 0
        times = 0
        for num in nums:
            if times<nums.count(num):
                times = nums.count(num)
                majority_element = num
        return majority_element


    # 方法2，去重以后再查找
    def majorityElement2(self, nums) -> int:
        majority_element = 0
        times = 0
        new_nums = []
        for num in nums:
            if new_nums.count(num)==0:
                new_nums.append(num)
        for new_num in new_nums:
            if times<nums.count(new_num):
                times = nums.count(new_num)
                majority_element = new_num
        return majority_element


    # 方法3，简化方法2
    def majorityElement3(self, nums) -> int:
        for num in list(set(nums)):
            if nums.count(num)>len(nums)/2:
                return num
        return 0

sol = Solution()
print(sol.majorityElement3([2,2,1,1,1,2,2]))