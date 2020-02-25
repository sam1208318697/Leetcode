# 面试题40.最小的k个数
#
# 输入整数数组arr ，找出其中最小的k个数。
# 例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
# 示例1：
# 输入：arr = [3, 2, 1], k = 2
# 输出：[1, 2]或者[2, 1]
#
# 示例2：
# 输入：arr = [0, 1, 2, 1], k = 1
# 输出：[0]
#
# 限制：
# 0 <= k <= arr.length <= 1000
# 0 <= arr[i] <= 1000



class Solution:
    def getLeastNumbers(self, arr, k: int):
        return sorted(arr)[:k]