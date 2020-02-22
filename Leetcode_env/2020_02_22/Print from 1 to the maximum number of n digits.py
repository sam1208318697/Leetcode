# 面试题17.打印从1到最大的n位数
# 输入数字n，按顺序打印出从1到最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的3位数999。
#
# 示例1:
# 输入: n = 1
# 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 说明：
# 用返回一个整数列表来代替打印n为正整数



class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        end = int("9"*n) + 1
        for i in range(1,end):
            res.append(i)
        return res