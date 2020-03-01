# 707.设计链表

# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val和next。
# val是当前节点的值，next是指向下一个节点的指针 / 引用。如果要使用双向链表，则还需要一个属性prev以指示链表中的上一个节点。
# 假设链表中的所有节点都是0 - index的。

# 在链表类中实现这些功能：
# get(index)：获取链表中第index个节点的值。如果索引无效，则返回 - 1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为val的节点追加到链表的最后一个元素。
# addAtIndex(index, val)：在链表中的第index个节点之前添加值为val的节点。如果index等于链表的长度，则该节点将附加到链表的末尾。如果index大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引index有效，则删除链表中的第index个节点。


# 示例：
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2); // 链表变为1-> 2-> 3
# linkedList.get(1); // 返回2
# linkedList.deleteAtIndex(1); // 现在链表是1-> 3
# linkedList.get(1); // 返回3

class LinkedList():
    def __init__(self,x):
        self.val = x
        self.next = None


class MyLinkedList(object):

    def __init__(self,):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # 判断index是否大于整个链表长度
        length = 0
        p = self.next
        while p:
            p = p.next
            length = length + 1
        if index >= length:
            return -1

        i = self.next
        count = 0
        while i and count<index:
            i = i.next
            count = count + 1
        return i.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = LinkedList(val)
        i = self.next
        node.next = i
        self.next =node


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = LinkedList(val)
        i = self
        while i.next :
            i = i.next
        i.next = node


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        # 判断index是否大于整个链表长度
        length = 0
        p = self.next
        while p :
            p = p.next
            length = length + 1
        if index>length:
            return None


        node = LinkedList(val)
        i = self
        j = self.next
        count = 0
        while j and count<index:
            i = i.next
            j = j.next
            count = count + 1
        if i.next:
            node.next = j
        i.next = node


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        # 判断index是否大于整个链表长度
        length = 0
        p = self.next
        while p:
            p = p.next
            length = length + 1
        if index >= length:
            return None

        i = self
        j = self.next
        count = 0
        while j and count < index:
            i = i.next
            j = j.next
            count = count + 1
        i.next = j.next

    def printLinkedList(self):
        r = self.next
        while r :
            print(r.val)
            r = r.next






linkedlist = MyLinkedList()
linkedlist.addAtHead(1)
linkedlist.addAtTail(3)
linkedlist.addAtIndex(1,2)
linkedlist.printLinkedList()
print("---------------")

param = linkedlist.get(1)
print(param)

print("---------------")
linkedlist.deleteAtIndex(1)
param = linkedlist.get(1)
print(param)

