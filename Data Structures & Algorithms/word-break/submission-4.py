class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem={}
        def dfs(i):
            if i==len(s):
                return True
            if i in mem:
                return mem[i]
            for word in wordDict:
                m=len(word)
                if s[i:i+m]==word and dfs(i+m):
                    mem[i]=True
                    return mem[i]
            
            mem[i]=False
            return mem[i]
        
        return dfs(0)
                

        