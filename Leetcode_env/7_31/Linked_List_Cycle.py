# 141. 环形链表
# 给定一个链表，判断链表中是否有环。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        i = head
        j = head
        while j:
            i = i.next
            if j.next ==None:
                return False
            j = j.next.next
            if i == j :
                return True
        return False


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(8)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node2
sol = Solution()
print(sol.hasCycle(node1))