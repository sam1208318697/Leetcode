# 面试题52.两个链表的第一个公共节点
#
# 输入两个链表，找出它们的第一个公共节点。
#
# 注意：
# 如果两个链表没有交点，返回null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足O(n)时间复杂度，且仅用O(1)内存。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return headA
        if headA.next == None:
            while headB != None:
                if headB == headA:
                    return headB
                else:
                    headB = headB.next
            return headA
        if headB.next == None:
            while headA != None:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
            return headA

        ha = headA
        hb = headB
        la = []
        lb = []
        while ha != None:
            la.append(ha)
            ha = ha.next
        while hb != None:
            lb.append(hb)
            hb = hb.next
        i = len(la) - 1
        j = len(lb) - 1

        while la[i] == lb[j]:
            i = i - 1
            j = j - 1
            if i == -1:
                return headA

        while headA != None:
            if headA == la[i]:
                break
            else:
                headA = headA.next
        headA = headA.next
        return headA