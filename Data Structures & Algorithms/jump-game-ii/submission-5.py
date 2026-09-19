class Solution:
    def jump(self, nums: List[int]) -> int:
        memo={}
        def dfs(i):
            if i>=len(nums)-1:
                return 0
            if i in memo:
                return memo[i]
            mini=float('inf')
            for j in range(1,nums[i]+1):
                mini=min(mini,1+dfs(i+j))
            memo[i]=mini
            return mini
        return dfs(0)
        


            



        