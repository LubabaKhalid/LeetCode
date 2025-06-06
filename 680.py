class Solution:
    def validPalindrome(self, s: str) -> bool:
        def fun(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return fun(l+1,r) or fun(l,r-1)
            l+=1
            r-=1
        return True