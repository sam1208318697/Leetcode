# 160.相交链表
# 编写一个程序，找到两个单链表相交的起始节点。

# 注意：
# 如果两个链表没有交点，返回null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足O(n)时间复杂度，且仅用O(1)内存。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    # 方法1：遍历法（超时）
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        i = headA
        j = headB
        stack = []
        while i :
            stack.append(i)
            i = i.next

        while j :
            if stack.count(j) == 1:
                return j.val
            else:
                stack.append(j)
            j = j.next
        return None

    # 方法2：双指针遍历相交法
    # 创建两个指针 pA 和 pB，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
    # 当pA到达链表的尾部时，将它重定位到链表 B 的头结点 (你没看错，就是链表 B); 类似的，
    # 当pB到达链表的尾部时，将它重定位到链表 A 的头结点。
    # 若在某一时刻 pA 和 pB 相遇，则 pA/pB 为相交结点。
    def getIntersectionNode2(self, headA, headB):
        i = headA
        j = headB
        #重定向判断
        bool_i = False
        bool_j = False

        while i!=None or j!=None:

            if i != j:
                if i == None:
                    if bool_i == False:
                        i = headB
                        bool_i = True
                    else:
                        pass
                else:
                    i = i.next

                if j == None:
                    if bool_j == False:
                        j = headA
                        bool_j = True
                    else:
                        pass
                else:
                    j = j.next


            else:
                return i.val



node1 = ListNode(4)
node2 = ListNode(1)

node3 = ListNode(5)
node4 = ListNode(0)
node5 = ListNode(1)

node6 = ListNode(8)
node7 = ListNode(4)
node8 = ListNode(5)

node1.next = node2
node2.next = node6

node3.next = node4
node4.next = node5
node5.next = node6

# node6.next = node7
# node7.next = node8


sol = Solution()
print(sol.getIntersectionNode2(node1,node3))