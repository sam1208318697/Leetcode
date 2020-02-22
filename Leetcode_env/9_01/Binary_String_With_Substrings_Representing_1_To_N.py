# 1016.子串能表示从1到N数字的二进制串
# 给定一个二进制字符串S（一个仅由若干'0'和'1'构成的字符串）和一个正整数N.
# 如果对于从1到N的每个整数X，其二进制表示都是S的子串，就返回true，否则返回false。

# 示例1：
# 输入：S = "0110", N = 3
# 输出：true

# 示例2：
# 输入：S = "0110", N = 4
# 输出：false

# 提示：
# 1 <= S.length <= 1000
# 1 <= N <= 10 ^ 9


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        if S == '':
            return False
        for i in range(1,N+1):
            cur = bin(i)[2:]
            if cur not in S:
                return False
        return True
sol = Solution()
print(sol.queryString('0110',4))