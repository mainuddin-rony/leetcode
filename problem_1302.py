# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        total = 0
        nodes = [[root]]
        while len(nodes[-1]) > 0:
            node_list = nodes[-1]
            tmp = []
            for n in node_list:
                if n.left != None:
                    tmp.append(n.left)
                if n.right != None:
                    tmp.append(n.right)
            nodes.append(tmp)
        nodes.pop(-1)
        last = nodes.pop(-1)
        
        for l in last:
            total += l.val
        
        
        return total
            
