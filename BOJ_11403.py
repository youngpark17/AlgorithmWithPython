from sys import stdin,stdout
n = int(stdin.readline())

visited = [False for i in range(n)]
graph = [[] for i in range(n)]
ans = [[0 for i in range(n)] for j in range(n)]

def dfs(s):
    for next in graph[s]:
        if(visited[next]==False):
            visited[next] = True
            dfs(next)

## dfs 돌면서 방문되는거 list에 담아서 return 하면서 graph에 체크하자.
for i in range(n):
    tmp = list(map(int,stdin.readline().split()))
    for j in range(n):
        if(tmp[j]==1):
            graph[i].append(j)

for i in range(n):
    dfs(i)
    for j in range(n):
        if(visited[j]==True):
            ans[i][j] = 1
    for j in range(n):
        visited[j] = False

for i in range(n):
    for j in range(n):
        stdout.write(str(ans[i][j])+" ")
    stdout.write("\n")

