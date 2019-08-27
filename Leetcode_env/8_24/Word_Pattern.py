class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strList = str.split(" ")
        print(strList)
        if len(pattern) != len(strList):
            return False
        dict = {}
        i = 0
        while i < len(pattern):
            s = pattern[i]
            if s not in dict:
                if dict == {}:
                    dict[s] = strList[i]
                    i = i + 1
                else:
                    if strList[i] in dict.values():
                        return False
                    else:
                        dict[s] = strList[i]
                        i = i + 1

            else:
                if dict[s] != strList[i]:
                    return False
                else:
                    i = i + 1
        return True


sol = Solution()
print(sol.wordPattern("abba","dog cat cat dog"))