# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def in_order(node):
            if node != None:
                in_order(node.right)
                # print(node.val)
                total = nodes.pop(0)
                total += node.val
                nodes.append(total)
                node.val = total
                in_order(node.left)
                
        nodes = [0]
        in_order(root)
        return root
        
