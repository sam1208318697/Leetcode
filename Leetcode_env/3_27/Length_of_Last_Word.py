# 58. 最后一个单词的长度
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5


def lengthOfLastWord(s: str) -> int:
    list = []
    count = 0
    if len(s) == 0 or (len(s) == 1 and s[0]==' '):
        return count
    elif len(s) == 1:
        return count+1
    elif len(s)>1 :
        #将字符串变成列表
        for i in s:
            list.append(i)
        #将列表末尾的所有空格去掉
        while list[-1] == ' ' :
            list.pop()
            if len(list) == 0:
                return count
        #保证列表最后一位不是空格后，从后往前数，遇到空格停止计数。
        for i in range(len(list)-1,-1,-1):
            if list[i] != ' ':
                count  = count + 1
            else:
                return count
    return count

print(lengthOfLastWord("hello world"))


