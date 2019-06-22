# 54. 螺旋矩阵
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

# 示例 1:
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]

# 示例 2:
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        up_row = 0
        down_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1
        res = []

        while up_row <= down_row and left_col <= right_col:

            # 从左到右
            for i in range(left_col, right_col + 1):
                res.append(matrix[up_row][i])
            up_row += 1
            if up_row > down_row:
                break

            # 从上到下
            for i in range(up_row, down_row + 1):
                res.append(matrix[i][right_col])
            right_col -= 1
            if left_col > right_col:
                break

            # 从右到左
            for i in range(right_col, left_col - 1, -1):
                res.append(matrix[down_row][i])
            down_row -= 1

            # 从下到上
            for i in range(down_row, up_row - 1, -1):
                res.append(matrix[i][left_col])
            left_col += 1


        return res


sol = Solution()
print(sol.spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]))