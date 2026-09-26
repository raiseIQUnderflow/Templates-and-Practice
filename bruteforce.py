# a = [4 ,5 ,8 ,8 ,8 ,4, 4 ,5 ,2, 3]
# b = [4, 5, 8, 2, 8, 4, 3, 5, 2, 3]
# n = len(a)
# from template import *
# with open('debug.txt', 'w') as f:
#     for i in range(1, 500001):
#         f.write(f"{i}\n")
    
import math
# # print(True)
    
    # s=set()
    # for i in range(1, 10001):
    #     o,e=0,0
        
    #     for j in range(1, i+1):
    #         if i%j == 0:
    #             if j&1:
    #                 o+=1 
    #             else:
    #                 e+=1 
    #     if e%o == 0:
    #         f.write(f"{o}\n")
    #         s.add(o)
val=4/5
# print(math.asin(val) * 180/math.pi )
def power(a, b, m=int(1e9+7)):
    '''to return a^b%m in O(logn) time'''
    res=1
    a %= m
    while b:
        if b % 2 == 1:
            res=(res*a) % m
        a=(a*a) % m
        b=b // 2
    return res % m

def fun(s):
    n=0 
    for i in s:
        n+=power(int(i),2)
    return int(n)

val=4
ans=0
with open('debug.txt', 'w') as f:
    for i in range(100):

            val=fun(str(val))
            ans+=1
            
            f.write(f"{val}\n")
