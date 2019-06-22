# 349. 两个数组的交集
# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]

# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]

# 说明:
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。



class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        if len(nums1) <= len(nums2):
            for i in nums1:
                if nums2.count(i) != 0:
                    res.append(i)
        else:
            for i in nums2:
                if nums1.count(i) != 0:
                    res.append(i)
        return res






sol = Solution()
print(sol.intersection([4,9,5],[9,4,9,8,4]))