class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res=0
        dp={}
        def dfs(i):
            if i==len(nums)-1:
                return True
            for j in range(1,nums[i]+1):
                if i in dp:
                    return dp[i]
                if i+j<len(nums) and dfs(i+j):
                    dp[i]=True
                    return dp[i]
            dp[i]=False
            return dp[i]
        return dfs(0)
        