class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        lst=[]
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        q=collections.deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node=q.popleft()
            lst.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
            
        
        
        if len(lst) == numCourses:
            return lst
        return []
        

    


        