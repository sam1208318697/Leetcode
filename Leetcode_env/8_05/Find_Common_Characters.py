# 1002.查找常用字符

# 给定仅有小写字母组成的字符串数组A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
# 例如，如果一个字符在每个字符串中出现3次，但不是4次，则需要在最终答案中包含该字符3次。
# 你可以按任意顺序返回答案。

# 示例1：
# 输入：["bella", "label", "roller"]
# 输出：["e", "l", "l"]

# 示例2：
# 输入：["cool", "lock", "cook"]
# 输出：["c", "o"]

# 提示：
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j]是小写字母


class Solution:
    def commonChars(self, A):
        if A == []:
            return []

        res = []
        S = list(set(list(A[0])))
        for s in S:
            cur = []
            for i in range(len(A)):
                cur.append(A[i].count(s))
            if cur.count(0) == 0:
                for i in range(min(cur)):
                    res.append(s)

        return res


sol = Solution()
print(sol.commonChars(["cool", "lock", "cook"]))