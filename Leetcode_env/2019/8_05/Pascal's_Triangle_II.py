# 119. 杨辉三角 II
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:
# 输入: 3
# 输出: [1,3,3,1]

# 进阶：
# 你可以优化你的算法到 O(k) 空间复杂度吗？

class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        res = [1, 1]
        i = 2
        while i <= rowIndex + 1:
            cur = []
            for a in range(i):
                if a == 0:
                    cur.append(1)
                elif a == i - 1:
                    cur.append(1)
                else:
                    cur.append(res[a - 1] + res[a])

            res = cur
            i = i + 1

        return res

sol = Solution()
print(sol.getRow(8))