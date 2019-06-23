# 345. 反转字符串中的元音字母
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

# 示例 1:
# 输入: "hello"
# 输出: "holle"

# 示例 2:
# 输入: "leetcode"
# 输出: "leotcede"

# 说明:
# 元音字母不包含字母"y"。

class Solution(object):
    # 方法1 ，可行但是太慢
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur = []
        pos = []
        for i,val in enumerate(s):
            if val.lower() == "a" or val.lower() == "e" or val.lower() == "i" or val.lower() == "o" or val.lower() == "u" :
                pos.append(i)
                cur.append(val)

        cur.reverse()
        index = 0
        S = list(s)
        for i,val in enumerate(S):
            if i in pos:
                S[i] = cur[index]
                index +=1

        return ''.join(S)

    # 方法2,前后指针
    def reverseVowels2(self, s):
        if s=='':return ''
        S = list(s)

        i = 0 # 前指针
        j = len(S)-1 # 后指针

        while i != j:
            if S[i].lower() == "a" or S[i].lower() == "e" or S[i].lower() == "i" or S[i].lower() == "o" or S[i].lower() == "u":
                while S[j].lower() != "a" and S[j].lower() != "e" and S[j].lower() != "i" and S[j].lower() != "o" and S[j].lower() != "u":
                    j = j - 1
                if i != j:
                    S[i], S[j] = S[j], S[i]
                    j = j - 1
                if i == j:
                    break
            i += 1
        return ''.join(S)








sol = Solution()
print(sol.reverseVowels2(''))


