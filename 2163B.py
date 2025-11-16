
def main():
    t = si()
    output_list = []
    for _ in range(t):
        n=si() 
        a=li() 
        x=list(ss()) 
        temp=[] 
        f=True
        s=['0']*n
        for i in range(n):
            if x[i]=='1':
                
                temp+=[a[i]] 

        
        if not temp:
            output_list+=[0]
            continue        
        # print(temp)
        m1,m2=max(temp), min(temp)
        l,r=0,n-1 
        while l<n:
            if a[l]<m2:
                break
            l+=1 
        while r>=0:
            if a[r]>m1:
                break
            r-=1 
        
        if l<r:
            for i in range(l+1, r):
                if a[l]<a[i]<a[r]:
                    s[i]='1' 
            f=True
            for i in range(n):
                if x[i]=='1':
                    if s[i]!='1':
                        f=False
                        break
            if f:
                output_list+=[1]
                output_list += [' '.join(map(str, [l+1, r+1])).strip()]
                continue
        
        l,r=0,n-1 
        while l<n:
            if a[l]>m1:
                break
            l+=1 
        while r>=0:
            if a[r]<m2:
                break
            r-=1 
        if l<r:
            for i in range(l+1, r):
                if a[r]<a[i]<a[l]:
                    s[i]='1' 
            f=True
            for i in range(n):
                if x[i]=='1':
                    if s[i]!='1':
                        f=False
                        break
            if f:
                output_list+=[1]
                output_list += [' '.join(map(str, [l+1, r+1])).strip()]
            else:
                output_list+=[-1]
        else:
            output_list+=[-1]

    print('\n'.join(map(str, output_list)).strip())
    pass

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
mod = 1e9+7
def input(): return sys.stdin.readline().strip()


BUFSIZE = 4096


#Fast IO using PyRival

RANDOM = random.randrange(2**62)


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
                os.fstat(self._fd).st_size, BUFSIZE))
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
                os.fstat(self._fd).st_size, BUFSIZE))
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
        return input().strip()
    return str(types)


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