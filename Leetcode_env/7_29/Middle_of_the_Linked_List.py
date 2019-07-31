# 876.链表的中间结点

# 给定一个带有头结点head的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。

# 示例1：
# 输入：[1, 2, 3, 4, 5]
# 输出：此列表中的结点3(序列化形式：[3, 4, 5])返回的结点值为3。
#     (测评系统对该结点序列化表述是[3, 4, 5])。
#     注意，我们返回了一个ListNode类型的对象ans，这样：ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及ans.next.next.next = NULL.

# 示例2：
# 输入：[1, 2, 3, 4, 5, 6]
# 输出：此列表中的结点4(序列化形式：[4, 5, 6])由于该列表有两个中间结点，值分别为3和4，我们返回第二个结点。

# 提示：
# 给定链表的结点数介于1和100之间。




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        length = 0
        i = head
        while i :
            length = length + 1
            i = i.next


        times = length//2
        j = head
        while times != 0:
            j = j.next
            times = times - 1

        return j







node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(8)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
# node4.next = node5
# node5.next = node6

sol = Solution()
print(sol.middleNode(node1).val)
