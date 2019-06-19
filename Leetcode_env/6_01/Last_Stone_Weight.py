#1046. 最后一块石头的重量
#有一堆石头，每块石头的重量都是正整数。
#每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

#如果 x == y，那么两块石头都会被完全粉碎；
#如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
#最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。



#提示：

#1 <= stones.length <= 30
#1 <= stones[i] <= 1000



import heapq

class Solution:

    # 方法一,直接使用list的排序方法进行处理
    def lastStoneWeight(self, stones):
        while len(stones) > 1:

            stones.sort()

            if stones[len(stones) - 1] == stones[len(stones) - 2]:
                stones.pop()
                stones.pop()
            else:
                last = stones[len(stones) - 1] - stones[len(stones) - 2]
                stones.pop()
                stones.pop()
                stones.append(last)
                stones.sort()

        if len(stones) == 1:
            return stones[0]
        else:
            return 0

    # ——————————————————分割线——————————————————

    # 该题在解法上使用了推排序的原理，引入了python标准库自带的堆模块heapq
    # 具体有关该模块的具体方法介绍请看：https://www.jianshu.com/p/801318c77ab5

    def lastStoneWeight2(self, stones):

        heap = []
        #对stones进行默认最小堆创建，因此我们存入数据时，将每个数据都乘以-1，则绝对值最大的数就在最小堆的根元素
        for i in stones:
            heapq.heappush(heap,i*(-1))
        #记录石头个数
        left_stones = len(stones)

        #当石头个数小于等于一个时，停止循环
        while left_stones>1:
            #弹出heap堆中最小的一个元素，「实为弹出的是最大的元素，因为全部加了负号」
            first = heapq.heappop(heap)
            #，同理，再弹出一个，
            second = heapq.heappop(heap)

            #对弹出的这两个数进行比较
            if first==second:
                left_stones = left_stones - 2
            else:
                heapq.heappush(heap,first - second)
                left_stones = left_stones - 1
        #返回结果
        #如果剩余一个，则返回那个结果的倒数（因为之前所有数全部都是乘以-1的），若石头相撞完则返回0
        if left_stones==1:
            return heapq.heappop(heap)*(-1)
        else:
            return  0



sol = Solution()
print(sol.lastStoneWeight([2,3,1]))
print(sol.lastStoneWeight2([2,3,1]))





