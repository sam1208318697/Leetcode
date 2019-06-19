#917. 仅仅反转字母

# 给定一个字符串S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

# 示例1：
# 输入："ab-cd"
# 输出："dc-ba"

# 示例2：
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"

# 示例3：
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"

# 思路：
# 我们先把整个字符串变成列表，然后识别出整个列表中的所有字母，将其放入另一个列表中，并再使用一个列表记录字母位置。
# 然后我们将全部是字母的列表进行反转，并根据之前记录的位置进行一一的替换
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # 创建一个列表，先把字符串变成列表
        list = []
        for i in S:
            list.append(i)
        print(list)

        # 我们将创建 存放字母 的列表a 和 存放每个字母在原先列表中的位置 的列表pos
        a=[]
        pos = []
        for i in range(len(list)):
            #判断是否为字母
            if  list[i].isalpha():
                a.append(list[i])
                pos.append(i)
            else:
                pass
        # 将全部是字母的列表进行反转
        a.reverse()
        print(a)
        print(pos)

        for i in range(len(pos)):
            list[pos[i]] = a[i]


        SS = ''.join(list)

        return SS




sol = Solution()
print(sol.reverseOnlyLetters('Qedo1ct-eeLg=ntse-T!'))