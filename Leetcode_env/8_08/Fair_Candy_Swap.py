# 888.公平的糖果交换

# 爱丽丝和鲍勃有不同大小的糖果棒：A[i]是爱丽丝拥有的第i块糖的大小，B[j]是鲍勃拥有的第j块糖的大小。
# 因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。
# （一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
# 返回一个整数数组ans，其中ans[0]
# 是爱丽丝必须交换的糖果棒的大小，ans[1]是Bob必须交换的糖果棒的大小。
# 如果有多个答案，你可以返回其中任何一个。保证答案存在。

# 示例1：
# 输入：A = [1, 1], B = [2, 2]
# 输出：[1, 2]

# 示例2：
# 输入：A = [1, 2], B = [2, 3]
# 输出：[1, 2]

# 示例3：
# 输入：A = [2], B = [1, 3]
# 输出：[2, 3]

# 示例4：
# 输入：A = [1, 2, 5], B = [2, 4]
# 输出：[5, 4]

# 提示：
# 1 <= A.length <= 10000
# 1 <= B.length <= 10000
# 1 <= A[i] <= 100000
# 1 <= B[i] <= 100000
# 保证爱丽丝与鲍勃的糖果总量不同。
# 答案肯定存在。



class Solution:
    # 普通法：超时
    def fairCandySwap(self, A, B):
        ans = []

        A.sort()
        B.sort()

        res = (sum(A)+sum(B))//2


        if sum(A)>sum(B):
            cha = sum(A) - res
            for i in A:
                for j in B:
                    if i - j == cha:
                        ans.append(i)
                        ans.append(j)
                        return ans

        elif sum(A)<sum(B):
            cha = sum(B) - res
            for i in B:
                for j in A:
                    if i - j == cha:
                        ans.append(j)
                        ans.append(i)
                        return ans
        else:
            for i in A:
                if i in B:
                    ans.append(i)
                    ans.append(i)
                    return ans

    # 方法2：使用set集合+数学运算

    # 设爱丽丝和鲍勃分别总计有 SA,SB 的糖果。
    # 如果爱丽丝给了糖果x，并且收到了糖果y，那么鲍勃收到糖果x并给出糖果y。那么，我们一定有 SA−x+y=SB−y+x
    # 对于公平的糖果交换。这意味着y=x+（SB−SA)/2
    # 我们的策略很简单。对于爱丽丝拥有的每个糖果x，如果鲍勃有糖果y=x+（SB−SA)/2,我们就返回 [x，y]。
    # 我们在常量时间内使用集 Set 结构来检查Bob是否拥有所需的糖果y。
    def fairCandySwap2(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]











sol = Solution()
print(sol.fairCandySwap2([2],[1,3]))
