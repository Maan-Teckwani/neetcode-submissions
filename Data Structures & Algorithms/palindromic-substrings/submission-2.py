class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        set1=set()
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                set1.add(s[l:r+1])
                count+=1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if s[l:r+1] not in set1:
                    count+=1
                l-=1
                r+=1
        return count

        