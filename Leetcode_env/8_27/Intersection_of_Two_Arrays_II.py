# 350. 两个数组的交集 II
# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]

# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 说明：输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。我们可以不考虑输出结果的顺序。

# 进阶:
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

class Solution:
    def intersect(self, nums1, nums2):
        res = []
        if len(nums1) > len(nums2):
            cur = nums1
            pos = nums2
        else:
            cur = nums2
            pos = nums1
        dict = {}
        for i in cur:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in pos:
            if i in dict:
                if dict[i] >= 1:
                    dict[i] -= 1
                    res.append(i)
        return res


sol  = Solution()
print(sol.intersect([1,2,2,1],[1,2,3,4,5,6]))



