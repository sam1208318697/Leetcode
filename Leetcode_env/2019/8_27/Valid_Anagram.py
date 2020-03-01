# 242. 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true

# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:你可以假设字符串只包含小写字母。
# 进阶:如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？


class Solution:
    # 字典法
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in t:
            if i not in dict:
                return False
            else:
                dict[i] -= 1

        for k, v in dict.items():
            if v != 0:
                return False
        return True
    # 字典序直接比较法
    def isAnagram2(self,s,t):
        return True if sorted(s) == sorted(t) else False

sol = Solution()
print(sol.isAnagram2("rat","car"))


