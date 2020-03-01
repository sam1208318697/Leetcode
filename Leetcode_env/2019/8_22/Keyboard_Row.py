# 500.键盘行
# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

# 示例：
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]

# 注意：
# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。

class Solution:
    def findWords(self, words):
        res = []
        array = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"], ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
                 ["z", "x", "c", "v", "b", "n", "m"]]

        for word in words:
            flag = True
            if word[0].lower() in array[0]:
                for i in word:
                    if i.lower() not in array[0]:
                        flag = False
                        break
            elif word[0].lower() in array[1]:
                for i in word:
                    if i.lower() not in array[1]:
                        flag = False
                        break
            else:
                for i in word:
                    if i.lower() not in array[2]:
                        flag = False
                        break


            if flag == True:
                res.append(word)
        return res

sol = Solution()
print(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]))

