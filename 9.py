class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x==0:
            return True
        else:
            s=str(x)
            s2=s[::-1]
            if s==s2:
                return True
            return False