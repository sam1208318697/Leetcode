# 203. 移除链表元素

# 删除链表中等于给定值 val 的所有节点。

# 示例:
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        root = ListNode(-1)
        root.next = head
        i = root
        j = root.next
        while j:
            if j.val == val:
                i.next = j.next
                j = j.next
            else:
                i = i.next
                j = j.next
        return root.next



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
sol = Solution()
print(sol.removeElements(node1,6))