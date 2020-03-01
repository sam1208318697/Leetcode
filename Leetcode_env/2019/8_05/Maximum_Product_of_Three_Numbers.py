# 628. 三个数的最大乘积
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

# 示例 1:
# 输入: [1,2,3]
# 输出: 6

# 示例 2:
# 输入: [1,2,3,4]
# 输出: 24

# 注意:
# 给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

class Solution:
    def maximumProduct(self, nums) -> int:
        if len(nums) == 3:
            return nums[0]* nums[1]*nums[2]
        # 负数集合（消去负号了）
        l1 = []
        # 正数集合
        l2 = []
        for i in nums:
            if i <= 0:
                l1.append(abs(i))
            else:
                l2.append(i)

        # 负数集合长度小于1等于一个
        if len(l1) <= 1:

            res = 1
            l2.sort()
            for i in range(3):
                res = res * l2[-1]
                l2.pop()
            return res
        # 正数集合长度大于3的情况
        elif len(nums)-2 > len(l1) > 1:

            res1 = 1
            res2 = 1

            for i in range(2):
                res2 = res2 * max(l1)
                l1.remove(max(l1))
            res2 = res2 * max(l2)


            for i in range(3):
                res1 = res1 * max(l2)
                l2.remove(max(l2))

            return max(res1, res2)
        # 正数集合长度小于3的情况
        elif len(nums) > len(l1) >= len(nums)-2:
            res = 1
            for i in range(2):
                res = res * max(l1)
                l1.remove(max(l1))
            res = res * max(l2)
            return res
        # 全负数的情况
        else:
            res = -1
            for i in range(3):
                res = res * min(l1)
                l1.remove(min(l1))
            return res


sol = Solution()
print(sol.maximumProduct([1,0,100]))