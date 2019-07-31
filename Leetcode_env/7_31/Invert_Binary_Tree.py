# 226. 翻转二叉树
# 翻转一棵二叉树。

# 示例：
# 输入：
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# 输出：
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归解法
    def invertTree(self, root: TreeNode):
        if root == None:
            return None
        p = TreeNode(root.val)
        p.left = self.invertTree(root.right)
        p.right = self.invertTree(root.left)
        return p

    # 迭代解法
    # 我们需要交换树中所有节点的左孩子和右孩子。因此可以创建一个队列来存储所有左孩子和右孩子还没有被交换过的节点。
    # 开始的时候，只有根结点在里面，只要这个队列不空，就一直从队列中出队节点，
    # 然后互换这个节点的左右孩子节点，接着再把孩子节点入队到队列中，对于其中空节点不需要加入队列
    # 最终队列一定会为空，这个时候所有节点的孩子节点都被互换过了，直接返回最初的根结点就好了。
    def invertTree2(self,root: TreeNode):

        if root == None:
            return None
        queue = [root,]
        while queue :
            i = queue.pop(0)
            i.left,i.right = i.right,i.left
            if i.left!= None:
                queue.append(i.left)
            if i.right != None:
                queue.append(i.right)
        return root




node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

sol = Solution()
print(sol.invertTree(node1))