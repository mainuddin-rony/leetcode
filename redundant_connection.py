class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1] * len(edges)
        
        def find_parent(x):
            if parent[x] == -1:
                return x
            else:
                return find_parent(parent[x])
        
        for edge in edges:
            x = find_parent(edge[0]-1)
            y = find_parent(edge[1]-1)
            
            if x != y:
                parent[y] = x
            
            else:
                return edge
