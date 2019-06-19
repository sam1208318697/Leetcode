# 437. 路径总和 III
# 给定一个二叉树，它的每个结点都存放着一个整数值。
# 找出路径和等于给定数值的路径总数。
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

# 示例：
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# 返回 3。和等于 8 的路径有:
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 分析：用到了两个递归 第一个递归：用于遍历每个结点 第二个递归：从该节点开始向下找存在的路径个数
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.f(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def f(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        res = 0
        if sum == root.val:
            res += 1
        res += self.f(root.left, sum - root.val) + self.f(root.right, sum - root.val)
        return res





root = [10,5,-3,3,2,0,11,3,-2,0,1]
node = []
for i in range(len(root)):
    node.append(TreeNode(root[i]))
node[0].left  = node[1]
node[0].right = node[2]
node[1].left  = node[3]
node[1].right = node[4]
node[2].left  = node[5]
node[2].right = node[6]
node[3].left  = node[7]
node[3].right = node[8]
node[4].left  = node[9]
node[4].right = node[10]



sol = Solution()
print(sol.pathSum(node[0],8))









