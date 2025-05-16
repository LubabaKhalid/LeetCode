class Solution:
    def reverse(self, x: int) -> int:
        start=-2**31
        end=(2**31)-1
        d=0
        y=abs(x)
        while y>0:
            d=d*10+y%10
            y=y//10
        if x<0:
            d=d*-1
        if d>=start and d<=end:
            return d
        return 0
