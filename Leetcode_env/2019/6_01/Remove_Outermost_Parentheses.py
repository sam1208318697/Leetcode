# 1021. 删除最外层的括号
#
# 有效括号字符串为空("")、"(" + A + ")"或A + B，其中A和B都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()"和"(()(()))"都是有效的括号字符串。
#
# 如果有效字符串S非空，且不存在将其拆分为S = A + B的方法，我们称其为原语（primitive），其中A和B都是非空有效括号字符串。
#
# 给出一个非空有效字符串S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中P_i是有效括号字符串原语。对S进行原语化分解，删除分解中每个原语字符串的最外层括号，返回S 。



# 示例1：
# 输入："(()())(())"
# 输出："()()()"
# 解释：输入字符串为"(()())(())"，原语化分解得到"(()())" + "(())"，删除每个部分中的最外层括号后得到"()()" + "()" = "()()()"。


# 示例2：
# 输入："(()())(())(()(()))"
# 输出："()()()()(())"
# 解释：输入字符串为"(()())(())(()(()))"，原语化分解得到"(()())" + "(())" + "(()(()))"，删除每隔部分中的最外层括号后得到"()()" + "()" + "()(())" = "()()()()(())"。


# 示例3：
# 输入："()()"
# 输出：""
# 解释：输入字符串为"()()"，原语化分解得到"()" + "()"，删除每个部分中的最外层括号后得到"" + "" = ""。
#
#
# 提示：
# S.length <= 10000
# S[i]为"("或")"S是一个有效括号字符串




class Solution:
    def removeOuterParentheses(self, S: str):

        list = []
        remove_list = [0,]
        # 将左右括号分别以1和-1进行数字化，并存在一个列表中
        for i in S:
            if i == "(":
                list.append(1)
            else:
                list.append(-1)
        # 对列表的每一项进行相加，记录每次加完等于0的位置，若该位置不是最后一位，则将下一位一并记录，保存在remove_list中，
        add=0
        for i in range(len(list)):
            add = add + list[i]
            if  add == 0:
                remove_list.append(i)
                if i!=len(list)-1:
                    remove_list.append(i+1)
                else:
                    pass
            else:
                pass

        # 将remove_list中记录的每个位置所对应的list中全部置0
        for i in remove_list:
            list[i] = 0
        # 然后删除这些0元素
        for i in range(len(remove_list)):
            list.remove(0)

        # 此时的list保存的即为脱去括号后的答案，但保存方式依然是1和-1的形式，我们需要将他们还原回左右括号
        ans = []
        for i in range(len(list)):
            if list[i]==1:
                ans.append("(")
            else:
                ans.append(")")
        # 最后将ans的列表转换为字符串
        return ''.join(ans)



    # ——————————————————分割线——————————————————
    #方法二，更加清楚明了


    def removeOuterParentheses2(self, S: str) -> str:
        cur = 0
        res = ""
        for i in range(len(S)):
            if cur == 0:
                pre = i
            if S[i] == '(':
                cur += 1
            else:
                cur -= 1
            if cur == 0:
                bracket = S[pre:i + 1]
                res += bracket[1:-1]
        return res




sol = Solution()
print(sol.removeOuterParentheses('(())()'))
print(sol.removeOuterParentheses2('(())()'))
