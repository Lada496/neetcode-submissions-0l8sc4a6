class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            adj[v].append((u, w))

        visited = set()
        total = 0
        minHeap = [(0, edges[0][0])]

        while len(visited) < n and minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue
            
            visited.add(n1)
            
            total += w1

            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2, n2))
        
        return total if len(visited) == n else -1