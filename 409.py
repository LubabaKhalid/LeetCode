from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(set(s))==1:
            return len(s)
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        c=0
        flag=True
        for v in d.values():
            if v%2==0:
                c+=v
            elif v>2:
                if flag:
                    c=c+v
                    flag=False
                else:
                    c=c+v-1
            elif v==1 and flag:
                c+=1
                flag=False
        return c

