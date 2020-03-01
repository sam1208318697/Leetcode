# 1078.Bigram分词
# 给出第一个词first和第二个词second，考虑在某些文本text中可能以"first second third"形式出现的情况，其中second紧随first出现，third紧随second出现。
# 对于每种这样的情况，将第三个词"third"添加到答案中，并返回答案。

# 示例1：
# 输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
# 输出：["girl", "student"]

# 示例2：
# 输入：text = "we will we will rock you", first = "we", second = "will"
# 输出：["we", "rock"]

# 提示：
# 1 <= text.length <= 1000
# text由一些用空格分隔的单词组成，每个单词都由小写英文字母组成
# 1 <= first.length, second.length <= 10
# first和second由小写英文字母组成

class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        res = []
        array = text.split(" ")
        if len(array) <= 2:
            return res
        for i in range(len(array)-2):
            if array[i] == first and array[i+1] == second:
                res.append(array[i+2])
        return res

sol  = Solution()
print(sol.findOcurrences("we will we will rock you","we","will"))