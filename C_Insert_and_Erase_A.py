
def main():
    s=list(ss().lower())
    t=list(ss().lower())
    # c1=Counter(s)
    # c2=Counter(t)
    # f=True
    if s==t:
        print(0)
        return
    # for k,v in c2.items():
    #     if k=='a':
    #         continue

    #     if k not in c1:
    #             f=False 
    #             break
    #     if v!=c1[k]:
    #             f=False 
    #             break
    # if not f:
    #     print(-1)
    #     return
    temp1, temp2=[],[] 
    for i in s:
        if i!='a':
            temp1+=[i] 
    for j in t:
        if j!='a':
            temp2+=[j] 
    if temp1!=temp2:
        print(-1)
        return
    # print(temp1,temp2)
    temp3,temp4=[0]*(len(temp1)+1), [0]*(len(temp1)+1) 
    ans=0 
    temp=0 
    j=0
    for i in range(len(s)):
        if s[i]=='a':
            temp+=1 
        else:
            temp3[j]=temp 
            temp=0 
            j+=1 
    temp3[j]=temp
    temp=0 
    j=0
    for i in range(len(t)):  
        if t[i]=='a':
            temp+=1 
        else:
            temp4[j]=temp 
            temp=0 
            j+=1 
    temp4[j]=temp
    for i in range(len(temp3)):
        ans+=abs(temp3[i]-temp4[i])
    print(ans)

    



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


BUFsiZE = 4096


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
        return (input().strip())
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