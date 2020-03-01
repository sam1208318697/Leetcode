# 206. 反转链表
# 反转一个单链表。

# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 我的做法：使用了一个堆栈用来存储链表中的每个节点
    def reverseList(self, head: ListNode) -> ListNode:
        # 创建一个堆栈
        node_stack = []

        node = head
        # 将每个节点保存在堆栈中
        while node != None:
            node_stack.append(node)
            node = node.next

        # 创建一个头节点
        root = ListNode(-1)
        i = root
        # 循环将每个节点弹出堆栈
        while node_stack:
            # 取出后进堆栈的节点
            node = node_stack.pop()
            # 改变他们的next属性
            i.next = node
            i = i.next
            i.next = None

        return root.next


    # 评论中的高赞答案：详细解析见：https://blog.csdn.net/xyh269/article/details/70238501
    # 此方法使用了三个指针，进行联动遍历
    def reverseList2(self,head:ListNode) -> ListNode:
        pre = None
        cur = head
        while cur != None:
            n = cur.next
            cur.next = pre
            pre = cur
            cur = n
        return pre









node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()

print(sol.reverseList2(node1))

