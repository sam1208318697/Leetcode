# 234. 回文链表
# 请判断一个链表是否为回文链表。

# 示例 1:
# 输入: 1->2
# 输出: false

# 示例 2:
# 输入: 1->2->2->1
# 输出: true

# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        re = head
        if re == None:
            return True
        while re.next!=None:
            l.append(re.val)
            re = re.next
        l.append(re.val)

        l_copy = l.copy()
        l.reverse()
        if l_copy == l:
            return True
        return False


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4


sol = Solution()
print(sol.isPalindrome(node1))