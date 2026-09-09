# from collections import *
y=932418
x=932418
# print(x+y-2*x,y+y-2*x,sep=' ')
d=set()
for i in range(1001):
    # d[y%x]+=1
    d.add(y%x)
    print(y,x,y%x,sep=' ')
    y+=1 
    x+=1
print(len(d))
