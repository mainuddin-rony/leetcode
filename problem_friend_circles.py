class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        parent = [-1] * len(M)
        graph = {}
        
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    if i not in graph:
                        graph[i] = []
                        graph[i].append(j)
                    else:
                        graph[i].append(j)
        group = graph.copy()
        
        def find_parent(index):
            if parent[index] == -1:
                return index
            else:
                return find_parent(parent[index])
        
        def union(x,y):
            x_set = find_parent(x)
            y_set = find_parent(y)
            parent[y_set] = x_set
            
            if x_set not in group:
                if y_set not in group:
                    group[x_set] = [y_set]
                else:
                    group[x_set] = []
                    group[x_set] += group[y_set]
                    group.pop(y_set)
            else:
                if y_set not in group:
                    group[x_set] += [y_set]
                else:
                    group[x_set] += group[y_set]
                    group.pop(y_set)
            
            
        for i in graph:
            for j in graph[i]:
                x = find_parent(i)  
                y = find_parent(j)
                
                if x!= y:
                    union(x,y)
                        
        print(group)
        print(parent)
        
        return len(group)
