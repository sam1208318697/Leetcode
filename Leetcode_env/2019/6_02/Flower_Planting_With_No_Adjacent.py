# 1042. 不邻接植花
# 有 N 个花园，按从 1 到 N 标记。在每个花园中，你打算种下四种花之一。
# paths[i] = [x, y] 描述了花园 x 到花园 y 的双向路径。
# 另外，没有花园有 3 条以上的路径可以进入或者离开。
# 你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。
# 以数组形式返回选择的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1, 2, 3, 4 表示。保证存在答案。

#示例 1：
# 输入：N = 3, paths = [[1,2],[2,3],[3,1]]
# 输出：[1,2,3]

# 示例 2：
# 输入：N = 4, paths = [[1,2],[3,4]]
# 输出：[1,2,1,2]

# 示例 3：
# 输入：N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# 输出：[1,2,3,4]

# 提示：
# 1 <= N <= 10000
# 0 <= paths.size <= 20000
# 不存在花园有 4 条或者更多路径可以进入或离开。
# 保证存在答案



class Solution:
    def gardenNoAdj(self, N, paths):

        res = [0]*N# 最终结果
        list=[[] for _ in range(N)]# 生成二维列表，list[0]中的数字代表，第一个花园和哪些花园有链路
        #将之前给的路径全部变成每个点之间的邻接表，这里的减1是因为，给出的花园是以1开始的，而列表中的全部是以0开始的，整体减1就匹配了
        for path in paths:
            list[path[0]-1].append(path[1]-1)
            list[path[1]-1].append(path[0]-1)
        print(list)

        # 一共三个路径，所以在四种颜色中肯定有一种和他们的颜色不相同，排除后选剩余的即可
        for i in range(N):
            # 判断i节点能染什么颜色:
            used = [0] * 5
            # 判断哪些颜色已经被占用了
            for j in list[i]:
                used[res[j]] = 1
            # 能够选取的颜色:
            for color in range(1, 5):
                if used[color] == 0:
                    res[i] = color
                    break

        return res



sol = Solution()
print(sol.gardenNoAdj(5,[[1,2],[1,3],[1,4],[5,2],[2,4],[5,3],[3,4]]))