# 2. 两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = ListNode(0)
        r  = re
        carry = 0
        while l1 or l2:
            if l1 != None :
                x = l1.val
            else:
                x = 0

            if l2 != None:
                y = l2.val
            else:
                y = 0


            sum = carry + x + y
            carry = sum // 10
            r.next = ListNode(sum%10)
            r = r.next

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if carry > 0:
            r.next = ListNode(1)

        return re.next




two = ListNode(2)
four = ListNode(4)
three = ListNode(3)
two.next = four
four.next = three

five = ListNode(5)
six = ListNode(6)
five.next = six


sol = Solution()
print(sol.addTwoNumbers(two,five))