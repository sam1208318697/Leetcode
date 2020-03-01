# 557. 反转字符串中的单词 III
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
# 示例 1:
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc" 
# 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。


class Solution:
    # 效率略低，但可行
    def reverseWords(self, s: str) -> str:
        res = []
        cur = []

        for i in range (len(s)):

            if s[i] != ' ':
                cur.append(s[i])

            else:
                if cur != []:
                    cur.reverse()
                    res.append(''.join(cur))
                    res.append(' ')
                    cur = []

        if cur!=[]:
            cur.reverse()
            res.append(''.join(cur))


        return ''.join(res)

    # 尝试利用堆栈，因为堆栈的原理很容易实现翻转
    def reverseWords2(self, s: str) -> str:
        res = ''
        stack = []  # 建立一个堆栈
        for i in range(len(s)):
            if s[i] != " ":
                stack.append(s[i])  # 如果不为空格则入栈
            else:
                # 如果为空格，将之前所有入栈的元素一一弹出，直至栈再次为空
                while stack != []:
                    res = res + stack.pop()
                res = res + ' '  # 同时不忘记遍历过的空格
        # 将最后一个入栈的单词再如法炮制的弹出
        while stack != []:
            res = res + stack.pop()
        return res









sol = Solution()
print(sol.reverseWords2("Let's take LeetCode contest"))





