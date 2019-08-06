# 1051.高度检查器

# 学校在拍年度纪念照时，一般要求学生按照非递减的高度顺序排列。
# 请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以非递减高度排列的必要移动人数。

# 示例：
# 输入：[1, 1, 4, 2, 1, 3]
# 输出：3
# 解释：
# 高度为4、3和最后一个1的学生，没有站在正确的位置。

# 提示：
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100


class Solution:
    def heightChecker(self, heights) -> int:
        count = 0
        h = []
        h.extend(heights)
        h.sort()
        for i in range(len(heights)):
            if heights[i] != h[i] :
                count += 1
        return count

sol = Solution()
print(sol.heightChecker([1, 1, 4, 2, 1, 3]))