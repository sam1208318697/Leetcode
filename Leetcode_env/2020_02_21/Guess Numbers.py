# LCP1.猜数字
#
# 小A和小B在玩猜数字。小B每次从1, 2, 3中随机选择一个，小A每次也从1, 2, 3中选择一个猜。
# 他们一共进行三次这个游戏，请返回小A猜对了几次？
# 输入的guess数组为小A每次的猜测，answer数组为小B每次的选择。
# guess和answer的长度都等于3。
#
# 示例1：
# 输入：guess = [1, 2, 3], answer = [1, 2, 3]
# 输出：3
# 解释：小A每次都猜对了。
#
# 示例2：
# 输入：guess = [2, 2, 3], answer = [3, 2, 1]
# 输出：1
# 解释：小A只猜对了第二次。
#
# 限制：
# guess的长度 = 3
# answer的长度 = 3
# guess的元素取值为{1, 2, 3}之一。
# answer的元素取值为{1, 2, 3}之一。

class Solution:
    def game(self, guess, answer) -> int:
        res = 0
        for i in range(len(guess)):
            if guess[i] == answer[i] :
                res += 1
        return res