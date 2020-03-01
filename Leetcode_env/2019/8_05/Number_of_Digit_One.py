# 233. 数字 1 的个数
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

# 示例:
# 输入: 13
# 输出: 6
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0

        count = 0
        base = 1
        round  = n
        while round>0:

            weight = round%10
            round =round // 10
            count = count + round * base
            if weight == 1:
                count = count + (n%base) + 1
            elif weight > 1:
                count = count + base
            base = base * 10

        return count


sol = Solution()
print(sol.countDigitOne(534))