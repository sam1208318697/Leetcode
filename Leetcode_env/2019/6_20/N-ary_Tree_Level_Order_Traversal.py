# 429. N叉树的层序遍历
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
# 例如，给定一个 3叉树 :
#       1
#    /  |  \
#   3   2   4
#  /  \
# 5   6
# 返回其层序遍历:
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]



# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    # 非递归解法,和同目录下的二叉树层序遍历题目类似
    def levelOrder(self, root: Node):

        res = []
        if not root:
            return res
        nodes_list = [root]

        while nodes_list:
            nodes = []
            cur = []
            for node in nodes_list:
                cur.append(node.val)
                for child in node.children:
                    nodes.append(child)
            res.append(cur)
            nodes_list = nodes

        return res