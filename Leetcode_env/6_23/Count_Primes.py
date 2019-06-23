# 204. 计数质数
# 统计所有小于非负整数 n 的质数的数量。

# 示例:
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

class Solution:
    # 方法一，可行但会超时，速度慢
    def countPrimes(self, n: int) -> int:
        res = 0
        for i in range(2,n):
            count = 0
            for j in range(1,i):
                if i%j == 0:
                    count += 1
            if count == 1:
                res += 1
        return res



    # 方法二，厄多拉塞筛选法
    def countPrimes2(self, n: int) -> int:
        if n < 3:
            return 0
        else:
            # 首先生成了一个全部为1的列表
            output = [1] * n
            # 因为0和1不是质数,所以列表的前两个位置赋值为0
            output[0], output[1] = 0, 0
            # 此时从index = 2开始遍历,output[2]==1,即表明第一个质数为2,然后将2的倍数对应的索引
            # 全部赋值为0. 此时output[3] == 1,即表明下一个质数为3,同样划去3的倍数.以此类推.
            for i in range(2, int(n ** 0.5) + 1):
                if output[i] == 1:
                    m = i ** 2  # 起始点就是i平方
                    while m < n:  # 循环遍历到列表最后一个元素
                        output[m] = 0
                        m += i  # 循环间隔为i
            # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
        return sum(output)






sol = Solution()
print(sol.countPrimes2(10))


