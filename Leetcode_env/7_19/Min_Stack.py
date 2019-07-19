# 155. 最小栈
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。

# 示例:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minstack) == 0:
            self.minstack.append(x)
        elif self.minstack[-1]<x:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(x)


    def pop(self) -> None:
        if len(self.stack) == 0:
            return False
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


    def getStack(self):
        return self.stack


    def getMinstack(self):
        return self.minstack

minstack = MinStack()

minstack.push(1)
print(minstack.getStack())
print(minstack.getMinstack())

minstack.push(-2)
print(minstack.getStack())
print(minstack.getMinstack())

minstack.push(3)
print(minstack.getStack())
print(minstack.getMinstack())

print(minstack.top())
minstack.pop()
print(minstack.top())
print(minstack.getMin())