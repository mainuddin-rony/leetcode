class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [-1] * n
        redundant = []
        
        def find_parent(x):
            if parent[x] == -1:
                return x
            else:
                return find_parent(parent[x])
        
        for edge in connections:
            x = find_parent(edge[0])
            y = find_parent(edge[1])
            
            if x != y:
                parent[y] = x
            
            else:
                redundant.append(edge)
        
        print(parent)
        print(redundant)
        
        count = 0
        for p in parent:
            if p == -1:
                count += 1
        if len(redundant) >= count-1:
            return count-1
        else:
            return -1
