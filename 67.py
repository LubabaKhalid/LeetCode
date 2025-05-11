class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        carry=0
        s=''
        while i>=0 or j>=0 or carry:
            if i>=0:
                v1=int(a[i])
                i-=1
            else:
                v1=0
            if j>=0:
                v2=int(b[j])
                j-=1
            else:
                v2=0
            total=v1+v2+carry
            carry=total//2
            digit=total%2
            s=s+str(digit)
        return s[::-1]

s=Solution()
a=input()
b=input()
print(s.addBinary(a,b))
 