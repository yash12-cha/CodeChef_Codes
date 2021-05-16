T=int(input())
for i in range(T):
    n,k=map(int,input().split())
    l=[]
    for i in range(1,k+1):
        l.append(n%i)
    print(max(l))