'''
    Author: Sarvajnya Pujari
    Language: PyPy3
    GitHub: https://github.com/sarvajnya
'''

def main():
    t = si()
    # output_list = []
    for _ in range(t):
        n,k=li() 
        g=["U"]*n
        for i in range(n):
            g[i]=['U']*n
        # print(g) 
        f=True
        c,c2=0,0
        rem = n*n - k
        if rem==1:
            print('NO')
            continue
        if rem:

            for i in range(n):
                for j in range(n):
                    
                    if k:
                        k-=1 
                    else:
                        if i<n-1:
                            g[i][j]='D'
                            rem-=1
                        else:
                            if c&1:
                                g[i][j]='L'
                            else:
                                g[i][j]='R'
                            c+=1

                        # if j == n-1:
                        #     if (rem%n)&1:
                        #         if c1&1 and rem:
                        #             g[i][j]='U' 
                        #         elif c1&1==0 and rem>1:
                        #             g[i][j]='D'
                        #         else:
                        #             f=False 
                        #             # break
                        #         c1+=1
                        # else:
                        #     if c2&1 and rem:
                        #         g[i][j]='L'
                        #     elif c2&1==0 and rem>1:
                        #         g[i][j]='R'
                        #     else:
                        #         f=False
                        #         # break
                        #     c2+=1 
                        # rem-=1
                    # print(g, f, rem, sep=' ')
                # if not f:
                #     break
        
                        
        if f:
            
            if  rem&1:
                g[-1][-1]=g[-1][-2]
            print('YES')

            for i in range(n):
                print(''.join(g[i]))
        else:
            print('NO')
                            
                        
               


        

    # print('\n'.join(map(str, output_list)).strip())
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