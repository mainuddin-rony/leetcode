# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        nodes_val = []
        
        def preorder(node):
            if node != None:
                if node.val >= L and node.val <= R:
                    nodes_val.append(node.val)
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        return sum(nodes_val)
