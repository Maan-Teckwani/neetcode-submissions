class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max=cur_min=res=nums[0]

        for num in nums[1:]:
            a=num
            b=cur_max*num
            c=cur_min*num

            cur_max=max(a,b,c)
            cur_min=min(a,b,c)

            res=max(res,cur_max)
        
        return res

                    


        