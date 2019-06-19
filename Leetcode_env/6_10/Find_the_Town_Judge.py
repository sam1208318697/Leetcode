# 997. 找到小镇的法官
# 在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。
# 如果小镇的法官真的存在，那么：
#       小镇的法官不相信任何人。
#       每个人（除了小镇法官外）都信任小镇的法官。
#       只有一个人同时满足属性 1 和属性 2 。

# 给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。
# 如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。

# 示例 1：
# 输入：N = 2, trust = [[1,2]]
# 输出：2

# 示例 2：
# 输入：N = 3, trust = [[1,3],[2,3]]
# 输出：3

# 示例 3：
# 输入：N = 3, trust = [[1,3],[2,3],[3,1]]
# 输出：-1

# 示例 4：
# 输入：N = 3, trust = [[1,2],[2,3]]
# 输出：-1

# 示例 5：
# 输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# 输出：3


class Solution:
    # 方法1 ，硬解
    def findJudge(self, N, trust):

        all = []
        count = 0
        for i in range(1,N+1):
            all.append(i)

        for i in range(len(trust)):
            if all.count(trust[i][0])==1:
                all.remove(trust[i][0])

        if len(all) != 1:
            return -1
        else:
            for i in range(len(trust)):
                if trust[i][1] == all[0]:
                    count = count +1
            if count == N-1:
                return all[0]
            else:
                return -1



    # 利用图的出度和入度来判断
    def findJudge2(self, N, trust):
        a = [0 for i in range(N)] # 你相信的人
        b = [0 for i in range(N)] # 相信你的人

        for per in trust:
            a[per[1]-1] += 1
            b[per[0]-1] += 1
        print(a)
        print(b)

        for i in range(N):
            if a[i]==N-1 and b[i]==0:
                return i+1
        return -1




sol = Solution()
print(sol.findJudge2(3,[[1,3],[2,3],[3,1]]))