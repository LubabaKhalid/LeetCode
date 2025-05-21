m=int(input())
n=bin(m)
x=len(n)-3
y=abs(m - 2**x)
z=abs(m-2**(x-1))
print(bin(54))
if y<z:
    print(len(bin(y))-2)
else:
    print(len(bin(z))-2)