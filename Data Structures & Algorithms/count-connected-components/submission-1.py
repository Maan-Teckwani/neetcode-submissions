class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=collections.defaultdict(list)
        visit=set()

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        

        def bfs(node):
            q=collections.deque()
            q.append(node)
            visit.add(node)

            while q:
                n=q.popleft()
                for nei in adj[n]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
        
        res=0
        for node in range(n):
            if node not in visit:
                bfs(node)
                res+=1
        
        return res
                


    
        
            
        