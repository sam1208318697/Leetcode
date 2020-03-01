# 383. 赎金信
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。
# 如果可以构成，返回 true ；否则返回 false。
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

# 注意：
# 你可以假设两个字符串均只含有小写字母。
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


class Solution:

    # 方法1，直接求解
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = [i for i in magazine ]
        for i in ransomNote:
            if mag.count(i) != 0:
                mag.remove(i)
            else:
                return False
        return True


    # 方法2，类似于构建哈希表
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        a = [chr(ord('a') + i) for i in range(0, 26)] # 创建一个包含26个英文字符的列表
        print(a)
        for i in a:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

sol = Solution()
print(sol.canConstruct2('baa','aba'))