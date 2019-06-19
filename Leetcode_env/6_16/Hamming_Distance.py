# 461. 汉明距离
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
# 注意：
# 0 ≤ x, y < 231.

# 示例:
# 输入: x = 1, y = 4
# 输出: 2

# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 上面的箭头指出了对应二进制位不同的位置。


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 将数字先变成二进制，然后去掉头部的0b，再字符串化，再列表化
        list_x = list(str(bin(x))[2:])
        list_y = list(str(bin(y))[2:])
        # 判断哪个列表更长，再将长短之差用0补齐
        if len(list_x) > len(list_y):
            max_length = len(list_x)
            count = max_length - len(list_y)
            for i in range(count):
                list_y.insert(0,0)
        else:
            max_length = len(list_y)
            count = max_length - len(list_x)
            for i in range(count):
                list_x.insert(0, 0)
        # 循环遍历找出两个列表不同的地方
        dif  = 0
        for i in range(max_length):
            if int(list_x[i]) != int(list_y[i]):
                dif += 1

        return dif


    # 方法2，使用x^y按位异或（当两对应的二进位相异时，结果为1），然后转为二进制，
    # 再使用filter函数，配合lambda函数进行过滤匹配，最终转换为列表并求出列表长度。
    def hammingDistance2(self, x: int, y: int) -> int:
        return len(list(filter(lambda x: x == '1', bin(x ^ y))))


sol = Solution()
print(sol.hammingDistance(1,4))