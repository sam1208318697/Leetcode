# 1290.二进制链表转整数
#
# 给你一个单链表的引用结点head。链表中每个结点的值不是0就是1。已知此链表是一个整数数字的二进制表示形式。
# 请你返回该链表所表示数字的十进制值 。
#
# 示例1：
# 输入：head = [1, 0, 1]
# 输出：5
# 解释：
# 二进制数(101)转化为十进制数(5)
#
# 示例2：
# 输入：head = [0]
# 输出：0
#
# 示例3：
# 输入：head = [1]
# 输出：1
#
# 示例4：
# 输入：head = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# 输出：18880
#
# 示例5：
# 输入：head = [0, 0]
# 输出：0
#
# 提示：
# 链表不为空。
# 链表的结点总数不超过30。
# 每个结点的值不是0就是1。



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ""
        while head.next != None:
            res = res + str(head.val)
            head = head.next
        res = "0b" + res + str(head.val)
        return int(res,2)


