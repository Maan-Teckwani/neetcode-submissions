class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # No loops must be present and no node should be unconnected for it to be a tree
        s=collections.defaultdict(list)
        if len(edges)>(n-1):
            return False

        for i,j in edges:
            s[i].append(j)
            s[j].append(i)
        
        visit=set()
        def dfs(node,par):
            if node in visit:
                return False
            visit.add(node)
            for nei in s[node]:
                if nei==par:
                    continue
                if not dfs(nei,node):
                    return False
            
            return True
        
        return dfs(0,-1) and len(visit)==n

        


        
        