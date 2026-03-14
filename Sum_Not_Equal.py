
def main():
    t = si()
    output_list = []
    for _ in range(t):
        n=si() 
        a=li() 
        if len(set(a))  == 1 and a[0]==0:
            output_list.append(-1)
            continue
        if len(set(a))  == 1 :
                output_list+=[' '.join(map(str, [1,2,3])).strip()] 
                continue
        f=False
        if 0 in a:
            k=a.index(0)
            for j in a:
                if j!=0:
                    val=j 
                    break
            j=a.index(val) 
            for i in range(len(a)):
                if a[i]+a[j]!=a[k] and i!=j and j!=k and k!=i:
                    f=True
                    break
            if f:
                output_list+=[' '.join(map(str, [i+1, j+1, k+1])).strip()] 
            else:
                output_list.append(-1)
            continue
            

               
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    
                    if i!=j and i!=k and j!=k:
                        if a[i]+a[j]!=a[k]:
                            f=True
                            break
                if f:
                    break
            if f:
                break
        

        if f:
            output_list+=[' '.join(map(str, [i+1, j+1, k+1])).strip()] 
        else:
            output_list.append(-1)
     
        



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