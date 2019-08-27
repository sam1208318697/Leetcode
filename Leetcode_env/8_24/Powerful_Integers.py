# 970.强整数
# 给定两个正整数x和y，如果某一整数等于x ^ i + y ^ j，其中整数i >= 0且j >= 0，那么我们认为该整数是一个强整数。
# 返回值小于或等于bound的所有强整数组成的列表。
# 你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

# 示例1：
# 输入：x = 2, y = 3, bound = 10
# 输出：[2, 3, 4, 5, 7, 9, 10]
# 解释：
#     2 = 2 ^ 0 + 3 ^ 0
#     3 = 2 ^ 1 + 3 ^ 0
#     4 = 2 ^ 0 + 3 ^ 1
#     5 = 2 ^ 1 + 3 ^ 1
#     7 = 2 ^ 2 + 3 ^ 1
#     9 = 2 ^ 3 + 3 ^ 0
#     10 = 2 ^ 0 + 3 ^ 2

# 示例2：
# 输入：x = 3, y = 5, bound = 15
# 输出：[2, 4, 6, 8, 10, 14]

# 提示：
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10 ^ 6


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        if x == y == 1:
            if bound >= 2:
                return [2]
            else:
                return []
        elif x>1 and y==1:
            res = []
            i = 0
            flag = True
            while flag:
                cur = x**i + 1
                if cur <= bound:
                    res.append(cur)
                    i = i + 1
                else:
                    flag = False
            return sorted(set(res))
        elif x==1 and y>1:
            res = []
            i = 0
            flag = True
            while flag:
                cur = 1 + y**i
                if cur <= bound:
                    res.append(cur)
                    i = i + 1
                else:
                    flag = False
            return sorted(set(res))
        else:
            res = []
            flagI = True
            i = 0
            while flagI:
                j = 0
                flagJ = True
                if x**i + y**j <= bound:
                    while flagJ:
                        cur = x**i + y**j
                        if cur <= bound:
                            res.append(cur)
                            j = j + 1
                        else:
                            flagJ = False
                    i = i + 1
                else:
                    flagI = False
            return sorted(set(res))
sol = Solution()
print(sol.powerfulIntegers(1,2,2))


