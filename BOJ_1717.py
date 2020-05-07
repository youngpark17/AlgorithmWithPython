from sys import stdin,stdout
n,m = map(int, stdin.readline().split())
parents = [i for i in range(0,n+1)]
def find(x):
    if(parents[x]==x):
        return x
    k = find(parents[x])
    parents[x] = k
    return k

def union(x,y):
    x=find(x)
    y=find(y)
    if(x!=y):
        if(x>y):
            parents[y] = x
        else:
            parents[x] = y




while(m!=0):
    m-=1
    c,a,b = map(int,stdin.readline().split())
    if(c==0):
        ##a와 b를 합침
        union(a,b)
    else:
        a = find(a)
        b = find(b)
        if(a==b):
            stdout.write("YES\n")
        else:
            stdout.write("NO\n")
