# 709.转换成小写字母
# 实现函数ToLowerCase()，该函数接收一个字符串参数str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
#
# 示例1：
# 输入: "Hello"
# 输出: "hello"

# 示例2：
# 输入: "here"
# 输出: "here"

# 示例3：
# 输入: "LOVELY"
# 输出: "lovely"

class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for i in str:
            res = res + i.lower()
        return res
sol = Solution()
print(sol.toLowerCase("LOVELY"))