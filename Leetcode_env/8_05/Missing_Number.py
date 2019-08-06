# 268. 缺失数字

# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

# 示例 1:
# 输入: [3,0,1]
# 输出: 2

# 示例 2:
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8

# 说明:你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

class Solution:
    def missingNumber(self, nums) -> int:
        #我们将数组中的所有数插入到一个集合中，这样每次查询操作的时间复杂度都是O(1)的
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i


sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))