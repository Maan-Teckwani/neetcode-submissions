
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def recursion(i,total):
            if i>=len(nums):
                return 1 if total==target else 0
            if (i,total) in memo:
                return memo[(i,total)]
            memo[(i,total)]=recursion(i+1,total+nums[i])+recursion(i+1,total-nums[i])
            return memo[(i,total)]
        return recursion(0,0)
            
            
            
        
            
        