# 1089.复写零

# 给你一个长度固定的整数数组arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
# 注意：请不要在超过该数组长度的位置写入元素。
# 要求：请对输入的数组就地进行上述修改，不要从函数返回任何东西。



# 示例1：
# 输入：[1, 0, 2, 3, 0, 4, 5, 0]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1, 0, 0, 2, 3, 0, 0, 4]

# 示例2：
# 输入：[1, 2, 3]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1, 2, 3]

# 提示：
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9

class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i = 0
        while i<l-1:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i,0)
                i = i + 2
            else:
                i = i + 1

sol = Solution()
print(sol.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))