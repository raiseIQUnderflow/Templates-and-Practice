'''Longest substring with k distinct characters'''
from collections import defaultdict
import math


def solve(s,k):
    n=len(s)
    ans=-math.inf
    init_len = 0 
    d=defaultdict(int)
    for i in range(n):
        d[s[i]]+=1

        if len(d) == k:
            ans = max(ans, i - init_len+1)

        while len(d) > k:           
            if d[s[init_len]]:
                d[s[init_len]] -= 1
            if d[s[init_len]] == 0:
                del d[s[init_len]]
            init_len += 1

    return ans

print(solve('abcccfcc',2))