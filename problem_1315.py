# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def get_sum_of_grand_children(node):
            tmp_sum = 0
            if node.left != None:
                if node.left.left != None:
                    tmp_sum += node.left.left.val
                if node.left.right != None:
                    tmp_sum += node.left.right.val
            if node.right != None:
                if node.right.left != None:
                    tmp_sum += node.right.left.val
                if node.right.right != None:
                    tmp_sum += node.right.right.val
            return tmp_sum
        
        total = 0
        nodes = [root]
        
        while len(nodes) > 0:
            node = nodes.pop(0)
            if node.val %2 == 0:
                total += get_sum_of_grand_children(node)
            if node.left != None:
                nodes.append(node.left)
            if node.right != None:
                nodes.append(node.right)
        return total
                
        
        
            
            
                
        
        
