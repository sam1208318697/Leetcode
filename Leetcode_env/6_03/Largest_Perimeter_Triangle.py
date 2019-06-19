# 976. 三角形的最大周长
#
# 给定由一些正数（代表长度）组成的数组A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 如果不能形成任何面积不为零的三角形，返回0。
#
# 示例1：
# 输入：[2, 1, 2]
# 输出：5

# 示例2：
# 输入：[1, 2, 1]
# 输出：0

# 示例3：
# 输入：[3, 2, 3, 4]
# 输出：10

# 示例4：
# 输入：[3, 6, 2, 3]
# 输出：8


class Solution:
    # 弱智法
    def largestPerimeter(self, A) -> int:

        res = 0
        for i in range(len(A)-2):
            for j in range(i+1,len(A)-1):
                for k in range(j+1,len(A)):
                    if A[i]+A[j]>A[k] and A[i]+A[k]>A[j] and A[j]+A[k]>A[i]:
                        cur = A[i]+A[j]+A[k]
                        if cur>res:
                            res = cur
                        else:
                            pass
                    else:
                        pass
        return res

    # ——————————————————分割线——————————————————

    # 方法2

    def largestPerimeter2(self, A):

        A.sort()
        for i in range(len(A)-1,1,-1):
            if A[i-2] + A[i-1] > A[i] :
                return A[i]+A[i-1]+A[i-2]
            else:
                pass

        return 0



sol = Solution()
print(sol.largestPerimeter([3, 2, 1]))
print(sol.largestPerimeter2([3, 2, 1]))







