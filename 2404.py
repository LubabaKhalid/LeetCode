d={0:1,2:2,4:2}
x=min(d.items(), key=lambda x: (-x[1], x[0]))[0]
print(x)