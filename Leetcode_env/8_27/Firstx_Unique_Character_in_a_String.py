# 387.字符串中的第一个唯一字符

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 - 1。

# 案例:
# s = "leetcode"
# 返回 0

# s = "loveleetcode",
# 返回 2

# 注意事项：您可以假定该字符串只包含小写字母。


class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for k, v in dict.items():
            flag = True
            if v == 1:
                for i in range(len(s)):
                    if s[i] == k:
                        res = i
                        flag = False
                        break
                if flag == False:
                    break

        return res
sol = Solution()
print(sol.firstUniqChar("leetcode"))