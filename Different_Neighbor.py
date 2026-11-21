
def main():
    n=si() 
    a=li() 
    temp=[0] 
    for i in range(n-1):
        if a[i]!=a[i+1]:
            temp+=[i+1]
    # print(temp)
    ans=[math.inf]*n
    for i in range(n):
        ind=bisect_left(temp,i)
        # print(a[i],ind,sep=' ') 
        if ind<len(temp):
            # print(ind)
            if temp[ind]!=i:
                ans[i]=min(ans[i],abs(temp[ind]-i))
            elif ind+1<len(temp):
                ans[i]=min(ans[i],abs(temp[ind+1]-i)) 
            
    # print(ans)
    a.reverse() 
    # print(a)
    temp=[0] 
    for i in range(n-1):
        if a[i]!=a[i+1]:
            temp+=[i+1]
    # print(temp)
    # ans=[math.inf]*n
    for i in range(n):
        ind=bisect_left(temp,i) 
        # print(a[i],ind,sep=' ') 
        if ind<len(temp):
            # print(ind)
            if temp[ind]!=i:
                ans[n-1-i]=min(ans[n-1-i],abs(temp[ind]-i))
            elif ind+1<len(temp):
                ans[n-1-i]=min(ans[n-1-i],abs(temp[ind+1]-i)) 
            
        # print(ans)
    print(*ans,sep=' ')

        # print(ind,temp[ind],sep=' ')



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