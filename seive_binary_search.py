from bisect import *

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def seive(n):
            r = [0]*(n+1)
            r[0] = r[1] = 1
            i = 2
            while i*i <= n:
                if not r[i]:
                    j = i*i
                    while j <= n:
                        r[j] = 1
                        j += i
                i += 1
            return r 
        
        n = 120000
        r = (seive(n))
        temp=[]
        for i in range(len(r)):
            if not r[i]:
                temp+=[i] 

        ans=0 
        n=len(nums)
        for i in range(n):
            if i&1:
                ind=bisect_left(temp, nums[i])
                if temp[ind] == nums[i]:
                    if nums[i]==2:
                        ans+=2 
                    else:
                        ans+=1
                
                          
                    

            else:
                    ind=bisect_left(temp, nums[i])
                    ans+=temp[ind]-nums[i]
                    
                    
        return ans

                
                
