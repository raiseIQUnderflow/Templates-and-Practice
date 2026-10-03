def diffArray(arr, opr):
    n = len(arr)

    # Convert arr to in-place difference array
    for i in range(n - 1, 0, -1):
        arr[i] -= arr[i - 1]

    # Apply each operation directly on the original array
    # Each operation is of the form [l, r, v]
    for l, r, v in opr:

        # Adding v at index l
        arr[l] += v

        # Subtracting v at index r + 1 ensures the addition 
        # stops at index r when prefix sums are applied
        if r + 1 < n:
            arr[r + 1] -= v

    # Take prefix sum to get the final updated array
    for i in range(1, n):
        arr[i] += arr[i - 1]

    return arr
    
def main():
    n,q=li() 
    res=[0]*(n+1 )
    d=defaultdict(list)
    upd=[]
    for i in range(q):
        l,r,x=li()
        d[x].append([l,r,1])
        
    for v in d:
        
        lst = d[v]
        
        lst.sort(key=lambda x: x[1])
        
        tmp = []
        for i in range(len(lst)):
            l, r,_ = lst[i]
            while tmp and min(tmp[-1][1], r) >= max(tmp[-1][0], l):
                nl, nr,__ = tmp.pop()
                l = min(nl, l)
                r = max(nr, r)
            
            tmp.append([l, r,1])
        upd.extend(tmp)
        
     
    
    print(*diffArray(res,upd)[1:],sep=' ')

    # print(d)
    
    # for i in range(n):



#Header_Files   
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
import math
mod=1e9+7
def input(): return sys.stdin.readline().strip()


BUFsiZE=4096


#Fast IO using PyRival

RANDOM=random.randrange(1<<61,1<<62)


def Wrapper(x):
  return x ^ RANDOM

class FastIO(IOBase):
    newlines=0

    def __init__(self, file):
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="x" in file.mode or "r" not in file.mode
        self.write=self.buffer.write if self.writable else None

    def read(self):
        while True:
            b=os.read(self._fd, max(
                os.fstat(self._fd).st_size, BUFsiZE))
            if not b:
                break
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(
                b), self.buffer.seek(ptr)
        self.newlines=0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b=os.read(self._fd, max(
                os.fstat(self._fd).st_size, BUFsiZE))
            self.newlines=b.count(b"\n") + (not b)
            ptr=self.buffer.tell()
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
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda s: self.buffer.write(s.encode("ascii"))
        self.read=lambda: self.buffer.read().decode("ascii")
        self.readline=lambda: self.buffer.readline().decode("ascii")


sys.stdout=IOWrapper(sys.stdout)


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