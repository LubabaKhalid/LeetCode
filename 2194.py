class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c=s[0]
        s1=int(s[1])
        r=s[3]
        r1=int(s[4])
        l=[]
        for i in range(ord(c),ord(r)+1):
            
            for j in range(s1,r1+1):
        
                l.append(chr(i)+str(j))
        return l
