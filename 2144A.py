
def main():
    t = si()
    output_list = []
    for _ in range(t):
        n=si() 
        a=li() 
        b=[i%3 for i in a]
        x,y,z=0,0,0 
        m,q,o=0,0,0 
        poss1=[]
        poss2=[]
        poss3=[]
        for i in range(n):
            x+=b[i] 
            y+=b[i] 
            z+=b[i] 
            if x%3 == 0 and m<2 and i+1 < n:
                m+=1 
                x=0
                poss1+=[i+1]



            if y%3 == 1 and q<2 and i+1 < n:
                q+=1
                y=0
                poss2+=[i+1]

            if z%3 == 2 and o<2 and i+1 < n:
                o+=1
                z=0
                poss3+=[i+1]
        # print(poss3,z,o,sep=' ')
        
        if x%3 == 0 and len(poss1) == 2:
            print(*poss1,sep=' ')
        elif  y%3 == 1 and len(poss2) == 2:
            print(*poss2,sep=' ')
        elif z%3 == 2 and len(poss3) == 2 :
            print(*poss3,sep=' ')  
        else:
            seen=set()
            s=0
            poss4=[]
            for i in range(n):
                s+=b[i] 
                if s%3 not in seen and len(seen) < 2 and i+1 < n:
                    seen.add(s%3)
                    s=0 
                    poss4+=[i+1]
            seen.add(s%3)
            if len(seen) == 3 :
                print(*poss4,sep=' ')   
            else:
                print(*[0,0],sep=' ')


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