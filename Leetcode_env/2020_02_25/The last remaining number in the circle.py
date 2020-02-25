# 面试题62.圆圈中最后剩下的数字
#
# 0, 1,, n - 1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
#
# 示例1：
# 输入: n = 5, m = 3
# 输出: 3
#
# 示例2：
# 输入: n = 10, m = 17
# 输出: 2
#
# 限制：
# 1 <= n <= 10 ^ 5
# 1 <= m <= 10 ^ 6

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        l = []
        for i in range(n):
            l.append(i)
        if len(l) == 1:
            return 0
        else:
            index = 0
            while len(l) != 1:
                count = 0
                while count < m-1:
                    if index < len(l)-1:
                        index += 1
                    else:
                        index = 0
                    count = count + 1
                if index < len(l)-1:
                    l.pop(index)
                else:
                    l.pop()
                    index = 0
            return l[0]

    def lastRemaining2(self, n: int, m: int) -> int:
        res = 0
        for i in range(2,n+1):
            res = (res+m)%i
        return res


sol = Solution()
print(sol.lastRemaining2(5,3))