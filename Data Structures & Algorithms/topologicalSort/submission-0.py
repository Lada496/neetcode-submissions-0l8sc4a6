class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        visit = set() # explored
        visiting = set() # detecting cycle
        topSort = []
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for u, v in edges:
            adj[u].append(v)

        def dfs(node):
            if node in visiting:
                return False
            
            if node in visit:
                return True
            
            visiting.add(node)

            for n in adj[node]:
                if not dfs(n):
                    return False
            
            visiting.remove(node)
            topSort.append(node)
            visit.add(node)
            return True
        
        for i in adj.keys():
            if not dfs(i):
                return []
        
        topSort.reverse()
        
        return topSort