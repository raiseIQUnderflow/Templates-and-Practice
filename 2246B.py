def fun(n):
    res=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            res.append(i)
            if i!=n//i:
                res.append(n//i)
    return res

def k_sum_exists(arr, k, target):
    
    
    def backtrack(start, k_left, target_left):
        # Base case: Found exactly k elements that hit the target
        if k_left == 0 and target_left == 0:
            return True
        # Base case: Exceeded element count or ran out of elements
        if k_left == 0 or start >= len(arr):
            return False
        
        # Optimization: If the smallest available element is larger than what's left, stop
        if arr[start] > target_left and arr[start] >= 0:
            return False
            
        for i in range(start, len(arr)):
            # Skip duplicates to avoid redundant paths
            if i > start and arr[i] == arr[i - 1]:
                continue
                
            # Include arr[i] and move to the next index
            if backtrack(i + 1, k_left - 1, target_left - arr[i]):
                return True
                
        return False

    return backtrack(0, k, target)



         
def main():
    t = si()
    output_list = []
    for _ in range(t):
        n=si()
        a=list(range(n,0,-1))
        k=1 
        r=[]
        f=False
        while k<=int(1e5):
            r=fun(k)
            if len(r)==n:
                print(k,r)
                if sum(r)==k:
                    f=True
                    break
            k+=1
        if not f:
            output_list.append(-1)
            continue
        output_list.append(' '.join(map(str, r)).strip())
        


    print('\n'.join(map(str, output_list)).strip())
    pass

import os
import sys
from io import BytesIO, IOBase

import random
import os

from bisect import *
from typing import *
from collections import *
from copy import *
from functools import *
from heapq import *
from itertools import *
from string import *
from math import *
mod = 1e9+7
def input(): return sys.stdin.readline().strip()


BUFsiZE = 4096


#Fast IO using PyRival

RANDOM = random.randrange(1<<62)


def Wrapper(x):
  return x ^ RANDOM

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(
                os.fstat(self._fd).st_size, BUFsiZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(
                b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(
                os.fstat(self._fd).st_size, BUFsiZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(
                b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdout = IOWrapper(sys.stdout)


def print(*args, end='\n', sep=''):
    for i in args:
        sys.stdout.write(str(i))
        sys.stdout.write(sep)
    sys.stdout.write(end)


def si(types=None):
    if not types:
        return int(input().strip())
    return int(types)


def sf(types=None):
    if not types:
        return float(input().strip())
    return float(types)


def ss(types=None):
    if not types:
        return list(input().strip())
    return list(str(types))


def li(types=None):
    if not types:
        return list(map(int, input().strip().split()))
    return list(map(int, str(types)))


def mi(types):
    return map(int, str(types))


def ms(types):
    return map(str, str(types))


def mf(types):
    return map(float, str(types))


def lf(types=None):
    if not types:
        return list(map(float, input().strip().split()))
    return list(map(float, str(types)))


def ls(types=None):
    if not types:
        return list(input().strip().split())
    return list(map(str, str(types)))

if __name__ == '__main__':
    main()