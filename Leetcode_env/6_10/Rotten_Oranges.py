# 994. 腐烂的橘子
#
# 在给定的网格中，每个单元格可以有以下三个值之一：
#   值 0 代表空单元格；
#   值 1 代表新鲜橘子；
#   值 2 代表腐烂的橘子。
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
#
#
# 示例 1：
# 输入：[[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# 输出：4
#
# 示例2：
# 输入：[[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# 输出：-1
# 解释：左下角的橘子（第2行， 第0列）永远不会腐烂，因为腐烂只会发生在4个正向上。
#
# 示例3：
# 输入：[[0, 2]]
# 输出：0
# 解释：因为0分钟时已经没有新鲜橘子了，所以答案就是0 。



class Solution:
    def orangesRotting(self, grid) -> int:

        minute = 0
        # 确定1和2的位置
        rotten_count = 0
        good_count = 0
        rotten_pos = []
        good_pos = []
        rooten_range = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 2:
                    rotten_count += 1
                    rotten_pos.append([i,j])
                elif grid[i][j] == 1:
                    good_count += 1
                    good_pos.append([i,j])
                else:
                    pass

        while good_count != 0:
            # 确定感染的范围
            for p in rotten_pos:
                if p[0] + 1 < len(grid) and grid[p[0] + 1][p[1]] == 1:
                    rooten_range.append([p[0] + 1 , p[1] ])

                if p[1] + 1 < len(grid[0]) and grid[p[0]][p[1] + 1] == 1:
                    rooten_range.append([p[0] , p[1] + 1 ])

                if p[0] - 1 >= 0 and grid[p[0] - 1][p[1]] == 1:
                    rooten_range.append([p[0] - 1, p[1]])

                if p[1] - 1 >= 0 and grid[p[0]][p[1] - 1] == 1:
                    rooten_range.append([p[0] , p[1] - 1 ])
            #进行感染
            if rooten_range != []:
                minute += 1
                for i in rooten_range:
                    grid[i[0]][i[1]] = 2

                # 更新1和2的位置
                rotten_count = 0
                good_count = 0
                rotten_pos = []
                good_pos = []
                rooten_range = []
                for i in range(len(grid)):
                    for j in range(len(grid[i])):

                        if grid[i][j] == 2:
                            rotten_count += 1
                            rotten_pos.append([i, j])
                        elif grid[i][j] == 1:
                            good_count += 1
                            good_pos.append([i, j])
                        else:
                            pass
            else:
                return -1

        return minute


sol = Solution()
print(sol.orangesRotting([[1],[2]]))