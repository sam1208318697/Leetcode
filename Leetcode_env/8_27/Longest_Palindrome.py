# 409. 最长回文串
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

# 注意:
# 假设字符串的长度不会超过 1010。

# 示例 1:
# 输入:"abccccdd"
# 输出:7

# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。



class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        l = list(dict.values())
        res = 0
        flag = False
        for i in l:
            if i % 2 == 0:
                res += i
            else:
                if i > 1:
                    flag = True
                    res = res + i - 1
                else:
                    flag = True
        if flag:
            res = res + 1

        return res


sol = Solution()
print(sol.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))