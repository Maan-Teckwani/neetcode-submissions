class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        out=[1]*len(nums)
        n=len(nums)
        for i in range(len(nums)):
            out[i]=left
            left*=nums[i]
        right=1
        for i in range(n-1,-1,-1):
            out[i]*=right
            right*=nums[i]
        return out
        
        