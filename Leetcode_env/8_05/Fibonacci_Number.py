# 509.斐波那契数

# 斐波那契数，通常用F(n)表示，形成的序列称为斐波那契数列。该数列由0和1开始，后面的每一项数字都是前面两项数字的和。也就是：
# F(0) = 0, F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中N > 1.给定N，计算F(N)。

# 示例1：
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.

# 示例2：
# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2.

# 示例3：
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3.

# 提示：
# 0 ≤ N ≤ 30

class Solution:
    # 方法1：递归法
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N > 1:
            return self.fib(N-1)+self.fib(N-2)

    # 方法2：列表循环法
    def fib2(self, N: int) -> int:
        f = [0, 1]
        if N == 0:
            return f[0]
        if N == 1:
            return f[1]
        i = 1
        while len(f) < N + 1:
            cur = f[i] + f[i - 1]
            f.append(cur)
            i = i + 1
        return f[-1]


sol = Solution()
print(sol.fib(30))