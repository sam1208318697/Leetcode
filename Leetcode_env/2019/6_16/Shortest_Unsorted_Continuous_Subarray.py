# 581. 最短无序连续子数组
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 你找到的子数组应是最短的，请输出它的长度。

# 示例 1:
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 说明 :
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。
class Solution:
    #  大佬做法，获取所有当前数组与排序后数组具有不同数值的索引，最右边的索引 - 最左边的 + 1 就是结果
    def findUnsortedSubarray(self, nums) -> int:
        res = []
        for i,(a,b) in enumerate(zip(nums,sorted(nums))):
            if a != b :
                res.append(i)
        if res == []:
            return 0
        return max(res) - min(res) + 1


sol = Solution()
print(sol.findUnsortedSubarray([2,3,3,2,4]))