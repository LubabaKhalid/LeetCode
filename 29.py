class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        c=0
        if abs(divisor)>abs(dividend):
            return 0
       
            
        negative=dividend<0 or divisor<0
        positive= dividend<0 and divisor<0
        dividend=abs(dividend)
        divisor=abs(divisor)
        if abs(divisor)!=1:
            while dividend>=divisor:
                dividend-=divisor
                c+=1
        else:
            c=abs(dividend)-1
        if positive:
            return c
        elif not positive and negative:
            return -c
        return c
s=Solution()
x=int(input())
y=int(input())
print(s.divide(x,y))