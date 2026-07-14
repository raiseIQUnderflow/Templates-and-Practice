
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(range(n, 0, -1))
        print(*a, sep=' ')
        


main()