# 231. 2的幂
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

# 示例 1:
# 输入: 1
# 输出: true
# 解释: 2^0 = 1

# 示例 2:
# 输入: 16
# 输出: true
# 解释: 2^4 = 16

# 示例 3:
# 输入: 218
# 输出: false



class Solution:
    # 正常思路
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        if n == 1:
            return True

        while n > 1:
            cur = n%2
            n = n//2
            if cur != 0:
                return False
        return True

    # 依托二进制，使用字符串解法，效率极高
    def isPowerOfTwo2(self, n: int) -> bool:
        cur = bin(n)[2:]
        if  n > 0:
            if cur.count('1') == 1:
                return True
            else:
                return False
        else:
            return False




sol = Solution()
print(sol.isPowerOfTwo2(1))