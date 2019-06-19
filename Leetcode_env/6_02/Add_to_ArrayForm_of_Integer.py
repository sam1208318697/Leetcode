# 989. 数组形式的整数加法

# 对于非负整数X而言，X的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果X = 1231，那么其数组形式为[1, 2, 3, 1]。
# 给定非负整数X的数组形式A，返回整数X + K的数组形式。


# 示例1：
# 输入：A = [1, 2, 0, 0], K = 34
# 输出：[1, 2, 3, 4]
# 解释：1200 + 34 = 1234

# 示例2：
# 输入：A = [2, 7, 4], K = 181
# 输出：[4, 5, 5]
# 解释：274 + 181 = 455

# 示例3：
# 输入：A = [2, 1, 5], K = 806
# 输出：[1, 0, 2, 1]
# 解释：215 + 806 = 1021

# 示例4：
# 输入：A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K = 1
# 输出：[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 解释：9999999999 + 1 = 10000000000

class Solution:
    def addToArrayForm(self, A, K: int):

        res = []# 最终答案
        num = 0

        if len(A)>10:
            return res

        # 将列表换成int型的数字
        for i in A:
            num = num*10+i
        # 相加
        num = num + K
        # 将结果再转换成列表
        while num > 0 :
            res.insert(0,num%10)
            num = num // 10

        if res == []:
            res.append(0)

        return res

    # ——————————————————分割线——————————————————


    # 方法2：逐位相加法

    # 让我们逐位将数字加在一起。
    # 举一个例子，如果要计算 123 与 912 的和。
    # 我们顺次计算 3+2、2+1、1+9。任何时候，当加法的结果大于等于 10 ，我们要将进位的 1 加入下一位的计算中去，所以最终结果等于 1035。

    # 我们可以对以上的想法做一个小变化，让它实现起来更容易 —— 我们将整个加数加入数组表示的数的最低位。
    # 继续之前的例子 123+912，我们把它表示成 [1, 2, 3+912]。
    # 然后，我们计算 3+912 = 915。5 留在当前这一位，将 910/10=91 以进位的形式加入下一位。
    # 然后，我们再重复这个过程，计算 [1, 2+91, 5]。我们得到 93，3 留在当前位，将 90/10=9 以进位的形式加入下一位。
    # 继而又得到 [1+9, 3, 5]，重复这个过程之后，最终得到结果 [1, 0, 3, 5]。

    def addToArrayForm2(self, A, K: int):

        A[-1] += K
        carry =0
        B=[]
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i > 0 :
                A[i - 1] += carry
        if carry > 0:
            for i in str(carry):
                B.append(int(i))
        A = B + A

        return A





    # ——————————————————分割线——————————————————

    #方法3：极简法
    #理解：
    # 第一步：使用map函数先将A中的每个元素进行字符化
    # 第二步：使用''.join()方法将所有元素均为字符形式的列表整体变成一个字符串
    # 第三步：将这个字符串使用int()方法再次数字化成一个整数，然后进行相加
    # 第四步：这时候结果已经产生，不过是int类型，我们先使用str()将其从数字类型再次变回一个字符串
    # 第五步：我们再次使用map()函数将这个字符串的每一位都int数字化
    # 第六步：将上一步中map()函数的返回值从迭代器进行列表化，最终返回结果

    def addToArrayForm3(self, A, K: int):

        return list(map(int,str(int(''.join(map(str,A)))+K)))




sol = Solution()
print(sol.addToArrayForm([2,1,5],9))
print(sol.addToArrayForm2([2,1,5],9))
print(sol.addToArrayForm3([2,1,5],9))