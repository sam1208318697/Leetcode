# 1351.统计有序矩阵中的负数
#
# 给你一个m * n的矩阵grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。
# 请你统计并返回grid中负数的数目。
#
# 示例1：
# 输入：grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
# 输出：8
# 解释：矩阵中共有8个负数。
#
# 示例2：
# 输入：grid = [[3, 2], [1, 0]]
# 输出：0
#
# 示例3：
# 输入：grid = [[1, -1], [-1, -1]]
# 输出：3
#
# 示例4：
# 输入：grid = [[-1]]
# 输出：1
#
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100


class Solution:
    def countNegatives(self, grid) -> int:
        if grid == [[]]:
            return 0
        hang = len(grid[0])
        lie = len(grid)
        res = 0
        for i in range(lie):
            for j in range(hang):
                if grid[i][j] >= 0:
                    pass
                else:
                    res = res + (hang - j)
                    break
        return res