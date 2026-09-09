class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm=set()
        for i in nums:
            if i in hm:
                return True
            hm.add(i)
        return False
        