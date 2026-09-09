class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1=[0]*26
        c2=[0]*26
        for ch in s:
            c1[ord(ch)-ord('a')]+=1
        for ch in t:
            c2[ord(ch)-ord('a')]+=1
        
        return c1==c2
        
        