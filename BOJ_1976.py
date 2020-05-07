from sys import stdin,stdout

n = int(stdin.readline())
m = int(stdin.readline())
graph = [[j for j in list(map(int,stdin.readline().split()))] for i in range(n)]
parents = [i for i in range(n)]

def find(x):
    if(x==parents[x]):
        return x
    k = find(parents[x])
    parents[x]=k
    return k

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        if(x>y):
            parents[y] = x
        else:
            parents[x] = y


for i in range(n):
    for j in range(n):
        if(graph[i][j]==1):
            union(i,j)

go = list(map(int,stdin.readline().split()))
st = set()
for i in go:
    st.add(find(i-1))

if(len(st)==1):
    print("YES")
else:
    print("NO")
