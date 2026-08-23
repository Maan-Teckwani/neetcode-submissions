class Solution:
    def isValid(self, s: str) -> bool:
        hmap={')':'(','}':'{',']':'['}
        st=[]
        for c in s:
            if c not in hmap:
                st.append(c)

            else:
                if st and st[-1]==hmap[c]:
                    st.pop()
                else:
                    return False
        
        return True if len(st)==0 else False