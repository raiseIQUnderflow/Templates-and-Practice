
def main():
    t = SI()
    output_list = []
    for _ in range(t):
        n=SI() 
        a=LI() 
        b=LI() 
        if a==b:
            output_list+=['YES']
            continue
        # f=True
        # for i in range(n-1):
        #     if a[i]==b[i]:
        #         continue
        #     if a[i]<b[i]:
        #         if a[i]>a[i+1] or a[i+1]>b[i]:
        #             a[i]=b[i] 
        #         else:
        #             a[i+1]=b[i]+1 
        #             a[i]=b[i]
        #     else:


        
        f=True
        for i in range(n):
            if a[i]==b[i]:
                continue

            if a[i]<b[i]:
                if b[i]>b[i+1]:
                    f=False
                    break
                a[i]=b[i]
            else:
                if i == 0:
                    if b[i]<=a[i+1]:
                        f=False
                        break
                a[i]=b[i]

        if a!=b:
            output_list += ['NO']
        else:
            output_list += ['YES']
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


def SI(types=None):
    if not types:
        return int(input().strip())
    return int(types)


def SF(types=None):
    if not types:
        return float(input().strip())
    return float(types)


def SS(types=None):
    if not types:
        return list(input().strip())
    return list(str(types))


def LI(types=None):
    if not types:
        return list(map(int, input().strip().split()))
    return list(map(int, str(types)))


def mi(types):
    return map(int, str(types))


def ms(types):
    return map(str, str(types))


def mf(types):
    return map(float, str(types))


def LF(types=None):
    if not types:
        return list(map(float, input().strip().split()))
    return list(map(float, str(types)))


def LS(types=None):
    if not types:
        return list(input().strip().split())
    return list(map(str, str(types)))
if __name__ == '__main__':
    main()