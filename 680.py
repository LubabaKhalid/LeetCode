s=input()
l=0
r=len(s)-1
c=0
while l<r:
    if s[l]!=s[r]:
        if c==0:
            if s[l]==s[r-1]:
                r-=1
            elif s[l+1]==s[r]:
                l+=1
            c=1
            
        else:
            print("NO")
            break
    else:
        l+=1
        r-=1
else:
    print("yes")