# 88.合并两个有序数组
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]





#---------------------弱智解法---------------------
# def merge(nums1, m, nums2, n) -> None:
#     # 给数组1进行除0操作
#     i = 0
#     while i < len(nums1):
#         if nums1[i] == 0:
#             nums1.pop(i)
#         else:
#             i = i + 1
#
#     # 将数组2中的每一个元素插入数组1中
#     j = 0
#     for num2 in nums2:
#         # 除0
#         if num2 == 0:
#             continue
#         # 若为最大，则放最后
#         if num2 > nums1[len(nums1) - 1]:
#             nums1.append(num2)
#             continue
#         # 若不为最大则，挨个寻找插入即可
#         while j < len(nums1):
#             if num2 <= nums1[j]:
#                 nums1.insert(i, num2)
#                 break
#             else:
#                 i = i + 1
#
#     print(nums1)
#
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# merge(nums1, 3, nums2, 3)




#---------------------正常解法---------------------
def merge1(nums1, m, nums2, n) -> None:

    #删去nums1中末尾的0元素
    while len(nums1)!=m:
        nums1.pop(len(nums1)-1)
    #将nums2中的数据先全部插入nums1中
    for j in range(0,n):
        nums1.append(nums2[j])
    #自动升序排序
    nums1.sort()
    print(nums1)

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge1(nums1, 3, nums2, 3)



#---------------------高级解法---------------------
def merge2(nums1, m, nums2, n) -> None:
    #sorted函数解释：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000
    #nums1[:m]指的是取0-m个元素
    nums1[:] = sorted(nums1[:m] + nums2)
    print(nums1)


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge2(nums1, 3, nums2, 3)