class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackPos=stack.pop()
                res[stackPos]=i-stackPos
            stack.append((t,i))
        return res

            
        
        
        