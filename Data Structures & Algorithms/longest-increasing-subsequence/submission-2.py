class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=0
        mem={}
        def dfs(i):
            if i in mem:
                return mem[i]
            best=1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    best=max(best,1+dfs(j))
                    mem[i]=best
            return best
        return max(dfs(i) for i in range(len(nums)))

                    


            