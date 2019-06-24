# 371. 两整数之和
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

# 示例 1:
# 输入: a = 1, b = 2
# 输出: 3

# 示例 2:
# 输入: a = -2, b = 3
# 输出: 1

class Solution:
    def getSum(self, a: int, b: int) -> int:



        # return a if b==0 else self.getSum(a^b,(a&b)<<1)
        return sum([a,b])


sol = Solution()
print(sol.getSum(14,-3))