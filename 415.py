class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n=self.strToInt(num1)
        m=self.strToInt(num2)
        return self.intToStr(n+m)
    def strToInt(self,a):
        if a=='0':
            return 0
        r=0
        for c in a:
            r=r*10+(ord(c)-ord('0'))
        return r
    def intToStr(self,a):
        if a==0:
            return '0'
        r=''
        while a>0:
            d=a%10
            r=chr(ord('0')+d)+r
            a=a//10
        return r

a=input()
b=input()      
s=Solution()
print(s.addStrings(a,b))
            