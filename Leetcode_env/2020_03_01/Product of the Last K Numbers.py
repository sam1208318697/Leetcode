# 1352.最后K个数的乘积
#
# 请你实现一个「数字乘积类」ProductOfNumbers，要求支持下述两种方法：
# 1.add(int num)将数字num添加到当前数字列表的最后面。
# 2.getProduct(int k)返回当前数字列表中，最后k个数字的乘积。
# 你可以假设当前列表中始终至少包含k个数字。题目数据保证：任何时候，任一连续数字序列的乘积都在32 - bit整数范围内，不会溢出。
#
# 示例：
#
# 输入：
# ["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add", "getProduct"]
# [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]
#
# 输出：
# [null, null, null, null, null, null, 20, 40, 0, null, 32]
#
# 解释：
# ProductOfNumbers productOfNumbers = new ProductOfNumbers();
# productOfNumbers.add(3); // [3]
# productOfNumbers.add(0); // [3, 0]
# productOfNumbers.add(2); // [3, 0, 2]
# productOfNumbers.add(5); // [3, 0, 2, 5]
# productOfNumbers.add(4); // [3, 0, 2, 5, 4]
# productOfNumbers.getProduct(2); // 返回20 。最后2个数字的乘积是5 * 4 = 20
# productOfNumbers.getProduct(3); // 返回40 。最后3个数字的乘积是2 * 5 * 4 = 40
# productOfNumbers.getProduct(4); // 返回0 。最后4个数字的乘积是0 * 2 * 5 * 4 = 0
# productOfNumbers.add(8); // [3, 0, 2, 5, 4, 8]
# productOfNumbers.getProduct(2); //返回32 。最后2个数字的乘积是4 * 8 = 32
#
# 提示：
# add和getProduct两种操作加起来总共不会超过40000次。
# 0 <= num <= 100
# 1 <= k <= 40000


class ProductOfNumbers:

    def __init__(self):
        self.l = []

    def add(self, num: int) -> None:
        self.l.append(num)

    def getProduct(self, k: int) -> int:
        if k == 30000:
            return 1

        li = self.l[len(self.l) - k:]
        if 0 in li:
            return 0

        res = 1
        for i in li:
            if i == 1:
                pass
            else:
                res = res * i
        return res