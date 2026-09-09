class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=0
        prod=1

        for num in nums:
            if num!=0:
                prod*=num
            else:
                zeros+=1
        if zeros>=2: return [0]*len(nums)

        res=[0]*len(nums)

        for i,c in enumerate(nums):
            if zeros:
                if c:
                    res[i]=0
                else:
                    res[i]=prod
            else:
                res[i]=prod//c
        return res

        