# 1160.拼写单词

# 给你一份『词汇表』（字符串数组）words和一张『字母表』（字符串） chars。
# 假如你可以用chars中的『字母』（字符）拼写出words中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
# 注意：每次拼写时，chars中的每个字母都只能用一次。返回词汇表words中你掌握的所有单词的长度之和。

# 示例1：
# 输入：words = ["cat", "bt", "hat", "tree"], chars = "atach"
# 输出：6
# 解释：可以形成字符串"cat"和"hat"，所以答案是3 + 3 = 6。

# 示例2：
# 输入：words = ["hello", "world", "leetcode"], chars = "welldonehoneyr"
# 输出：10
# 解释：可以形成字符串"hello"和"world"，所以答案是5 + 5 = 10。

# 提示：
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# 所有字符串中都仅包含小写英文字母
import copy

class Solution:
    def countCharacters(self, words, chars: str) -> int:
        dict = {}
        for i in chars:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        res = 0
        for word in words:
            flag = True
            d = copy.deepcopy(dict)
            for i in word:
                if i in d:
                    if d[i] > 1:
                        d[i] -= 1
                    else:
                        del d[i]
                else:
                    flag = False
                    break
            if flag == True:
                res += len(word)
        return res

sol = Solution()
print(sol.countCharacters(["hello","world","leetcode"],"welldonehoneyr"))
