# 面试题25. 合并两个排序的链表
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
# 示例1：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 限制：
# 0 <= 链表长度 <= 1000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        h = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                h.next = l2
                l2 = l2.next
            else:
                h.next = l1
                l1 = l1.next
            h = h.next
        if l2 != None:
            h.next = l2
        if l1 != None:
            h.next = l1
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

l1 = node1
l2 = node4

sol = Solution()
s = sol.mergeTwoLists(l1,l2)
while s != None:
    print(s.val)
    s = s.next