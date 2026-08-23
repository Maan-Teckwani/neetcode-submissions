class Solution:
    def isValid(self, s: str) -> bool:
        hmap={')':'(','}':'{',']':'['}
        st=[]
        for c in s:
            if c not in hmap:
                st.append(c)
            elif not st:
                return False
            else:
                if st[-1]==hmap[c]:
                    st.pop()
                else:
                    return False
        
        return True if len(st)==0 else False