import sys

n,m = map(int,sys.stdin.readline().split())

count=0
graph =[]

for i in range(n+1):
    graph.append([])
visited = []
for i in range(n+1):
    visited.append(False)
def dfs(x):
    visited[x] = True
    for next in graph[x]:
        if(not visited[next]):
            dfs(next)

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1,n+1):
    if visited[j]==False:
        dfs(j)
        count+=1;

print(count)

