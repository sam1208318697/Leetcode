# 面试题50.第一个只出现一次的字符
#
# 在字符串s中找出第一个只出现一次的字符。如果没有，返回一个单空格。
#
# 示例:
# s = "abaccdeff"返回"b"
# s = ""返回" "
#
# 限制：
# 0 <= s的长度 <= 50000

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if s == "":
            return " "
        else:
            dict = {}
            for i in s:
                if i not in dict:
                    dict[i] = 1
                else:
                    dict[i] += 1
            for k, v in dict.items():
                if v == 1:
                    return k
            return " "