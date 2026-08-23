class Solution(object):
    def findComb(self,ind,arr,target,ans,ds):
        if target==0:
            ans.append(list(ds))
            return
        for i in range(ind,len(arr)):
            if i > ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:
                break
            ds.append(arr[i])
            self.findComb(i+1,arr,target-arr[i],ans,ds)
            ds.pop()

    def combinationSum2(self, candidates, target):
        ans=[]
        candidates.sort()
        ds=[]
        self.findComb(0,candidates,target,ans,ds)
        return ans
        
        