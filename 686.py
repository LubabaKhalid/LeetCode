import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        t=math.ceil(len(b)/len(a))
        res=a*t
        if b in res:
            return t
        elif b in (res+a):
            return t+1
        return -1