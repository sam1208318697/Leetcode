# 202. 快乐数
#
# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
#
# 示例:
#
# 输入: 19
# 输出: true
# 解释:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1


def isHappy(n: int) -> bool:
    i = 0
    while i<100:
        ans = 0
        while n>=10:
            ans = ans + ( n % 10 ) * ( n % 10 )
            n = int( n / 10 )
        ans = ans + ( n * n )
        if ans == 1:
            return True
        else:
            n = ans
            i = i + 1
    return False


print(isHappy(190))





#大佬的循环解法
# 运算符中：//    表示向下取整
# 运算符中：**    表示乘方
def isHappy(n):

    num_list = {n}
    while (True):
        num = 0
        while (n >= 1):
            k = n % 10
            num = num + k ** 2
            n = n // 10
        if num == 1:
            return True
        elif num in num_list:
            return False
        else:
            num_list.add(num)
            n = num