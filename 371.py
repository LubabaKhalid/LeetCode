a=int(input())
b=int(input())

MASK=0x7FFFFFFF
MAX=0xFFFFFFFF
while b!=0:
    carry=(a & b) & MASK
    a=(a^b)&MASK
    b=(carry<<1)&MASK
if a<=MAX:
    print(a)
else:
    print(~(a^MASK))