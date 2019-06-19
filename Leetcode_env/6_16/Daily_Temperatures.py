# 739. 每日温度
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高的天数。如果之后都不会升高，请输入 0 来代替。
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的都是 [30, 100] 范围内的整数。





class Solution:
    # 方法一，超出时间限制
    def dailyTemperatures(self, T):
        t = []
        for i in range(len(T)-1,-1,-1):
            if i == len(T)-1:
                t.insert(0,0)
            else:
                count = 1
                for j in range (i+1,len(T)):
                    if T[j]>T[i]:
                        t.insert(0,count)
                        break
                    else:
                        count = count + 1
                if len(t) != (len(T)-i):
                    t.insert(0,0)
        return t

    # 方法二，用到堆栈，递减栈
    def dailyTemperatures2(self, T):
        stack = []
        r =  [0] * len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                r[stack.pop()] = i - stack[-1]
            stack.append(i)
        return r



sol = Solution()
print(sol.dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73]))