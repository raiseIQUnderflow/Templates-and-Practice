
def main():
    t = si()
    
    for _ in range(t):
        n,c=li() 
        a=li() 
        b=li() 
        f1=True 
        f2=True 
        ans1=0
        ans2=c
        for i in range(n):
            if a[i]>=b[i]:
                ans1+=(a[i]-b[i])
            else:
                f1=False
                ans1=0
                break
        
             
        a.sort()
        b.sort()
            
        
        for i in range(n):
            if a[i]>=b[i]:
                ans2+=(a[i]-b[i])
            else:
                f2=False
                ans2=0
                break
        if f1 and f2:
            print(min(ans1,ans2))
        elif f2:
            print(ans2)
        elif f1:
            print(ans1)
        else:
            print(-1)

    pass



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