# 66. 加一
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 例如：
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。

def plusOne(digits):
    #是否有进位
    jinwei=False
    for i in range(len(digits)-1,-1,-1):
        #若各位数字不等于0直接末尾数字加一返回即可
        if digits[i] != 9:
            digits[i] = digits[i]+1
            return digits

        elif digits[i] == 9:
            digits[i] = 0
            jinwei = True

        elif digits[i] == 9 and jinwei==True:
            digits[i] = 0
            jinwei = True

        else:
            digits[i] = digits[i]+1
            jinwei=False

    #防止[9,9,9,9]一进位变成[0,0,0,0]的情况出现
    ans = 0
    for j in digits:
        ans = ans + j
    if  ans == 0 :
        digits.insert(0,1)

    return digits


print(plusOne([9]))
