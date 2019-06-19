# 949. 给定数字能组成的最大时间

# 给定一个由4位数字组成的数组，返回可以设置的符合24小时制的最大时间。
# 最小的24小时制时间是00: 00，而最大的是23: 59。从00: 00 （午夜）开始算起，过得越久，时间越大。
# 以长度为5的字符串返回答案。如果不能确定有效时间，则返回空字符串。


# 示例1：
# 输入：[1, 2, 3, 4]
# 输出："23:41"

# 示例2：
# 输入：[5, 5, 5, 5]
# 输出：""



from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A):


        A.sort(reverse=True)
        print (A)
        p = permutations(A)# 输出可迭代的一种全排列的方法
        for hour1,hour2,min1,min2 in p:
            if hour1*10+hour2<24 and min1*10+min2<60:
                return str(hour1)+str(hour2)+':'+str(min1)+str(min2)
        return ''



sol = Solution()
print(sol.largestTimeFromDigits([2,9,3,0]))