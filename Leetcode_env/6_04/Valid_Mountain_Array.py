# 941. 有效的山脉数组

# 给定一个整数数组A，如果它是有效的山脉数组就返回true，否则返回false。
# 让我们回顾一下，如果A满足下述条件，那么它是一个山脉数组：
# A.length >= 3
# 在 0 < i < A.length - 1 条件下，存在i使得：
# A[0] < A[1] < ... < A[i - 1] < A[i]
# A[i] > A[i + 1] > ... > A[B.length - 1]

# 示例1:
# 输入：[2, 1]
# 输出：false

# 示例2：
# 输入：[3, 5, 5]
# 输出：false

# 示例3：
# 输入：[0, 3, 2, 1]
# 输出：true

class Solution:
    def validMountainArray(self, A) -> bool:
        # 如果长度小于3，直接返回错误
        if len(A)<3:
            return False
        #如果长度等于3，判断两边是否都小于中间，若是返回True
        elif len(A) == 3:
            if A[0]<A[1] and A[1]>A[2]:
                return True
            else:
                return False
        # 数组长度大于3
        else:
            # 找到数组中的最大值
            largest = max(A)
            # 找到这个最大值在数组的哪个位置
            pos = 0
            for i in range(len(A)):
                if  A[i] == largest:
                    pos = i
            # 判断这个位置是否是数组第一个或者数组最后一个，若是，返回False
            if pos == 0 or pos == len(A)-1:
                return False
            # 从最大值这个位置将数组一分为二，遍历前半边数组，是否满足每前一个都小于每后一个
            for i in range(pos):
                if A[i]>=A[i+1]:
                    return False
            # 遍历后半边数组，是否满足每前后个都小于每前一个
            for i in range(pos,len(A)-1):
                if A[i]<=A[i+1]:
                    return False
            return True







sol = Solution()
print(sol.validMountainArray([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]))