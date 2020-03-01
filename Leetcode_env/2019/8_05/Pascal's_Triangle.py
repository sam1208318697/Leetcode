# 118. 杨辉三角
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        i = 3
        while i <= numRows:
            cur = []
            for a in range(i):
                if a == 0:
                    cur.append(1)
                elif a == i - 1:
                    cur.append(1)
                else:
                    cur.append(res[i - 2][a - 1] + res[i - 2][a])

            res.append(cur)
            i = i + 1

        return res


sol = Solution()
print(sol.generate(6))