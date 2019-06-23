# 172. 阶乘后的零
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
# 示例 1:
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
# 示例 2:
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 说明: 你算法的时间复杂度应为 O(log n) 。


class Solution:
    # 方法一，超时
    def trailingZeroes(self, n: int) -> int:
        res = 0
        num = 1
        for i in range(1,n+1):
            num = num * i
        l = list(str(num))
        for i in range(len(l)-1,-1,-1):
            if l[i]=='0':
                res += 1
            else:
                break

        return res

    # 方法二，超时
    def trailingZeroes2(self, n: int) -> int:
        res = 0
        num = 1
        for i in range(1, n + 1):
            num = num * i
            while num%10 == 0:
                num = num // 10
                res = res + 1
        return res

    # 方法二，超时
    def trailingZeroes3(self, n: int) -> int:
        res = 0
        for i in range(1,n + 1):
            while i % 5 == 0:
                res = res+1
                i = i//5
        return res

    # 方法四，答案

    def trailingZeroes4(self, n: int) -> int:
        res = 0
        while n >= 5:
            res = res + int(n / 5)
            n = n // 5
        return res

    # 题目问阶乘的结果有几个零，如果用笨方法求出阶乘然后再算0的个数会超出时间限制。
    # 然后我们观察一下，5的阶乘结果是120，零的个数为1：
    # 5! = 5 * 4 * 3 * 2 * 1 = 120
    # 末尾唯一的零来自于2 * 5。很显然，如果需要产生零，阶乘中的数需要包含2和5这两个因子。
    # 例如：4 * 10 = 40也会产生零，因为4 * 10 = (2 * 2) * (2 * 5) 。
    # 因此，我们只要数一数组成阶乘的数中共有多少对2和5的组合即可。又因为5的个数一定比2少，问题简化为计算5的个数就可以了。



sol = Solution()
print(sol.trailingZeroes4(25))

