# 645. 错误的集合
# 集合 S 包含从1到 n 的整数。
# 不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。
# 你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

# 示例 1:
# 输入: nums = [1,2,2,4]
# 输出: [2,3]
# 注意:
# 给定数组的长度范围是 [2, 10000]。
# 给定的数组是无序的。


class Solution:
    # 列表法，超时
    def findErrorNums1(self, nums):
        res = []
        a = 0
        b = 0
        for i in range(1,len(nums)+1):
            if nums.count(i) == 2:
                a = i
            if i not in nums:
                b = i
        res.append(a)
        res.append(b)
        return res


    # 数学法
    def findErrorNums2(self, nums):
        res = []
        # 1到n求和
        sumA = sum([i for i in range(1,len(nums)+1)])
        # set集合求和
        sumB = sum(set(nums))
        # 原列表求和
        sumC = sum(nums)
        res.append(sumC - sumB)
        res.append(sumA - sumB)
        return res

sol = Solution()
print(sol.findErrorNums2([1,2,2,3]))


