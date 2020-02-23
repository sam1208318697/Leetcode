# 面试题24.反转链表
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
#
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 限制：
# 0 <= 节点个数 <= 5000

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        l = []
        while head != None:
            l.insert(0, head)
            head = head.next

        res = l[0]
        h = l[0]
        for i in range(1, len(l)):
            h.next = l[i]
            h = h.next
        h.next = None

        return res
