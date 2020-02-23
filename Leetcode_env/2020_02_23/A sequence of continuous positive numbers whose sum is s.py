# 面试题57 - II.和为s的连续正数序列
#
# 输入一个正整数target ，输出所有和为target的连续正整数序列（至少含有两个数）。序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#
# 示例1：
# 输入：target = 9
# 输出：[[2, 3, 4], [4, 5]]
#
# 示例2：
# 输入：target = 15
# 输出：[[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]
#
# 限制：
# 1 <= target <= 10 ^ 5


class Solution:
    def findContinuousSequence(self, target: int):
        res = []
        for i in range(1,target):
            l = [i]
            he = sum(l)
            a = i
            while he < target:
                l.append(a+1)
                he = sum(l)
                a = a + 1
            if he == target:
                res.append(l)
        return res