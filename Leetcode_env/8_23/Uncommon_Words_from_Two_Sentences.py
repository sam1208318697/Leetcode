# 884.两句话中的不常见单词

# 给定两个句子A和B。（句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
# 如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
# 返回所有不常用单词的列表。您可以按任何顺序返回列表。

# 示例1：
# 输入：A = "this apple is sweet", B = "this apple is sour"
# 输出：["sweet", "sour"]

# 示例2：
# 输入：A = "apple apple", B = "banana"
# 输出：["banana"]

# 提示：
# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A和B都只包含空格和小写字母。


class Solution:
    def uncommonFromSentences(self, A: str, B: str):

        listA = A.split(" ")
        listB = B.split(" ")

        dict = {}
        for i in listA:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for j in listB:
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
        res = []
        for k, v in dict.items():
            if v == 1:
                res.append(k)
            else:
                pass
        return res


sol = Solution()
print(sol.uncommonFromSentences("apple apple","this"))