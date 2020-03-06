# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:                   
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        def get_values(tree):
            tmp_nodes = []
            values = []
        
            values.append(tree.val)
            
            tmp_nodes.append(tree.left)
            tmp_nodes.append(tree.right)                  
            
            while len(tmp_nodes) > 0:
                node = tmp_nodes.pop(0)
                
                if node == None:
                    values.append('null')
                else:
                    values.append(node.val)
                    tmp_nodes.append(node.left)
                    tmp_nodes.append(node.right)
                
            return values  
    
        list_p = get_values(p)
        list_q = get_values(q)
        
        print(list_p)
        print(list_q)
        
        return list_p == list_q


        
        
            
        
