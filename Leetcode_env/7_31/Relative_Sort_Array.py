# 1122.数组的相对排序

# 给你两个数组，arr1和arr2，
# arr2中的元素各不相同
# arr2中的每个元素都出现在arr1中
# 对arr1中的元素进行排序，使arr1中项的相对顺序和arr2中的相对顺序相同。
# 未在arr2中出现过的元素需要按照升序放在arr1的末尾。

# 示例：
# 输入：arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2 = [2, 1, 4, 3, 9, 6]
# 输出：[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

# 提示：
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# arr2中的元素arr2[i]各不相同arr2中的每个元素arr2[i]都出现在arr1中


class Solution:
    def relativeSortArray(self, arr1, arr2):
        res = []
        for i in arr2:
            while i in arr1:
                res.append(i)
                arr1.remove(i)
        arr1.sort()
        res = res + arr1
        return (res)


sol = Solution()
print(sol.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],[2, 4, 3, 9, 6]))