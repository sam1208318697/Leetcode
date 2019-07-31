# 83. 删除排序链表中的重复元素
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# 示例 1:
# 输入: 1->1->2
# 输出: 1->2

# 示例 2:
# 输入: 1->1->2->3->3
# 输出: 1->2->3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode):
        if head == None:
            return None
        i = head
        j = head.next
        while j:
            if i.val == j.val:
                i.next = j.next
                j = j.next
            else:
                i = j
                j = j.next

        r = head
        while r:
            print(r.val)
            r = r.next 
        return head








node1 = ListNode(1)
# node2 = ListNode(1)
# node3 = ListNode(1)
# node4 = ListNode(2)
# node5 = ListNode(4)
# node6 = ListNode(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6

sol = Solution()
print(sol.deleteDuplicates(node1))