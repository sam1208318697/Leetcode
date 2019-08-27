# 953.验证外星语词典
# 某种外星语也使用英文小写字母，但可能顺序order不同。字母表的顺序（order）是一些小写字母的排列。
# 给定一组用外星语书写的单词words，以及其字母表的顺序order，只有当给定的单词在这种外星语中按字典序排列时，返回true；否则，返回false。

# 示例1：
# 输入：words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# 输出：true
# 解释：在该语言的字母表中，'h'位于'l'之前，所以单词序列是按字典序排列的。

# 示例2：
# 输入：words = ["word", "world", "row"], order = "worldabcefghijkmnpqstuvxyz"
# 输出：false
# 解释：在该语言的字母表中，'d'
# 位于'l'之后，那么words[0] > words[1]，因此单词序列不是按字典序排列的。

# 示例3：
# 输入：words = ["apple", "app"], order = "abcdefghijklmnopqrstuvwxyz"
# 输出：false
# 解释：当前三个字符"app"匹配时，第二个字符串相对短一些，然后根据词典编纂规则"apple" > "app"，因为'l' > '∅'，其中'∅'是空白字符，定义为比任何其他字符都小（更多信息）。

# 提示：
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# 在words[i]和order中的所有字符都是英文小写字母。

class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        for i in range(len(words) - 1):
            if len(words[i]) <= len(words[i + 1]):
                for j in range(len(words[i])):
                    if order.index(words[i][j]) > order.index(words[i + 1][j]):
                        return False
                    elif order.index(words[i][j]) < order.index(words[i + 1][j]):
                        break
                    else:
                        pass
            else:
                for j in range(len(words[i + 1])):
                    if order.index(words[i][j]) > order.index(words[i + 1][j]):
                        return False
                    elif order.index(words[i][j]) < order.index(words[i + 1][j]):
                        break
                    else:
                        if j == len(words[i + 1]) - 1:
                            return False
        return True


sol = Solution()
print(sol.isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz"))