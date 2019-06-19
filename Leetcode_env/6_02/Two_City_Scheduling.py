#1029. 两地调度
# 公司计划面试2N人。第i人飞往A市的费用为costs[i][0]，飞往B市的费用为costs[i][1]。
# 返回将每个人都飞到某座城市的最低费用，要求每个城市都有N人抵达。

# 示例：
# 输入：[[10, 20], [30, 200], [400, 50], [30, 20]]
# 输出：110
# 解释：
# 第一个人去A市，费用为10。第二个人去A市，费用为30。第三个人去B市，费用为50。第四个人去B市，费用为20。
# 最低总费用为10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。

# 提示：
# 1 <= costs.length <= 100
# costs.length为偶数
# 1 <= costs[i][0], costs[i][1] <= 1000



class Solution:
    def twoCitySchedCost(self, costs) -> int:

        res = 0# 最终结果（总费用）
        a_city = 0# 去A城市的人数
        b_clty = 0# 去B城市的人数
        half_len = len(costs)/2# 总人数的一半

        # 每安排一个人走，就将其在costs中删除，当删空costs列表代表全部人被分配完成
        while costs!=[]:

            cur = 0
            pos = 0
            # 在for循环中找出，每次差额最大的那一位在剩余列表中的位置
            for i in range(len(costs)):
                if cur < abs(costs[i][0]-costs[i][1]):
                    cur = abs(costs[i][0]-costs[i][1])
                    pos = i
                else:
                    pass
            #现根据去两个城市的金额多少进行分配，再根据两地报名人数的差额进行最终的安排
            if costs[pos][0]<costs[pos][1]:
                if a_city < half_len:
                    res = res + costs[pos][0]
                    a_city = a_city + 1
                else:
                    res = res + costs[pos][1]
                    b_clty = b_clty + 1
            else:
                if b_clty < half_len:
                    res = res + costs[pos][1]
                    b_clty = b_clty + 1
                else:
                    res = res + costs[pos][0]
                    a_city = a_city + 1
            # 安排完成，删除该目标
            costs.pop(pos)
        return res


sol = Solution()
print(sol.twoCitySchedCost([[10,20],[400,50],[200,30],[1000,20]]))