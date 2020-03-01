# 102. 二叉树的层次遍历
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 此为递归做法
    def levelOrder(self, root: TreeNode):
        res = []

        if not root:
            return res


        def loop(nodes_list):

            nodes = [] # 存放了下次需要遍历的全部节点
            cur = [] # 存放了当前一行的所有节点，之后会将这个保存到res中
            # 循环遍历当前一排的节点，并依次序生成下一排的节点列表
            for node in nodes_list:
                cur.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            # 将当前一排的节点保存到最终结果中
            res.append(cur)
            # 判断是否已经到了最终一排，
            if nodes == []:
                return
            # 递归循环
            loop(nodes)


        list = []
        list.append(root)
        loop(list)

        return res


root = [3,9,20,0,0,15,7]
nodes =[]
for node in root:
    nodes.append(TreeNode(node))

nodes[0].left  = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left  = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left  = nodes[5]
nodes[2].right = nodes[6]


sol = Solution()
print(sol.levelOrder(nodes[0]))