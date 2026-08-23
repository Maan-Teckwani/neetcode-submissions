class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=collections.defaultdict(list)

        def dfs(src,target,visit):
            if src==target:
                return True
            visit.add(src)
            for nei in adj[src]:
                if nei not in visit:
                    if dfs(nei,target,visit):
                        return True
            
            return False

        
        for u,v in edges:
            if u in adj and v in adj:
                visit=set()

                if dfs(u,v,visit):
                    return [u,v]
            
            adj[u].append(v)
            adj[v].append(u)
        