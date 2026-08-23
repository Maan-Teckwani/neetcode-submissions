class Solution(object):
    def findComb(self,ind,arr,target,ans,ds):
        if ind==len(arr):
            if target==0:
                ans.append(list(ds))
            return
        if arr[ind]<=target:
            ds.append(arr[ind])
            self.findComb(ind,arr,target-arr[ind],ans,ds)  #multiple inserts handling
            ds.pop()
        self.findComb(ind+1,arr,target,ans,ds)   #go to next element


    def combinationSum(self, arr, target):
        ans=[]
        ds=[]
        self.findComb(0,arr,target,ans,ds)
        return ans

         
        
        
        