# #914. 卡牌分组
#
# 给定一副牌，每张牌上都写着一个整数。
# 此时，你需要选定一个数字X，使我们可以将整副牌按下述规则分成1组或更多组：

# 每组都有X张牌。
# 组内所有的牌上都写着相同的整数。

# 仅当你可选的X >= 2时返回true。


# 示例1：
# 输入：[1, 2, 3, 4, 4, 3, 2, 1]
# 输出：true
# 解释：可行的分组是[1, 1]，[2, 2]，[3, 3]，[4, 4]

# 示例2：
# 输入：[1, 1, 1, 2, 2, 2, 3, 3]
# 输出：false
# 解释：没有满足要求的分组。

# 示例3：
# 输入：[1]
# 输出：false
# 解释：没有满足要求的分组。

# 示例4：
# 输入：[1, 1]
# 输出：true
# 解释：可行的分组是[1, 1]

# 示例5：
# 输入：[1, 1, 2, 2, 2, 2]
# 输出：true
# 解释：可行的分组是[1, 1]，[2, 2]，[2, 2]


class Solution:
    def func(self,list, x):
        li = []
        for i in range(len(list)):
            li.append(list[i] % x)
        print('li:')
        print(li)
        if max(li) == min(li) == 0:
            return True
        else:
            return False
    def hasGroupsSizeX(self, deck) -> bool:

        if len(deck) > 1:
            if min(deck)==max(deck):
                return True
            else:

                cur = []
                res = []
                for i in deck:
                    if cur.count(i)==0:
                        cur.append(i)
                    else:
                        pass
                for n in cur:
                    res.append(deck.count(n))
                if min(res) == max(res):
                    return True
                else:
                    print("res:")
                    print(res)
                    #求res数组中所有数字的最大公约数如果最大公约数不为1，则有结果
                    length = max(res)
                    for x in range(2,length):
                        if self.func(res,x):
                            return True
                    return False
        else:
            return False

sol = Solution()
print(sol.hasGroupsSizeX([0,0,0,1,1,1,1,1,1,2,2,2,3,3,3]))
