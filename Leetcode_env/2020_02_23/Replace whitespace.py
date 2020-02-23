# 面试题05.替换空格
#
# 请实现一个函数，把字符串s中的每个空格替换成"%20"。
#
# 示例1：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")