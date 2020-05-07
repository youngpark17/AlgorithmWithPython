from sys import stdin,stdout
import sys
sys.setrecursionlimit(10000)

m,n,k = map(int,stdin.readline().split())
graph = [[0 for i in range(n)] for j in range(m)]

dx = [0,0,1,-1]
dy = [-1,1,0,0]
visited  = [[False for i in range(n)] for j in range(m)]
def dfs(x,y):
    tmp=1
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(nx>=0 and ny>=0 and nx<m and ny<n):
            if(not visited[nx][ny] and graph[nx][ny]==0):
                tmp+=dfs(nx,ny)

    return tmp

while(k!=0):
    k-=1
    x1,y1,x2,y2 = map(int,stdin.readline().split())
    x1,y1=y1,x1
    x1=m-1-x1
    x2-=1
    y2-=1
    x2,y2=y2,x2
    x2=m-1-x2

    if(x2>x1):
        x1,x2=x2,x1
    if(y2>y1):
        y1,y2=y2,y1

    ## x1,y1이 항상 더 크다.
    for i in range(x2,x1+1):
        for j in range(y2,y1+1):
            graph[i][j] = 1

ans = []
count=0
for i in range(m):
    for j in range(n):
        if(graph[i][j]==0 and not visited[i][j]):
            ans.append(dfs(i,j))
            count+=1

ans = sorted(ans)
stdout.write(str(count)+"\n")
for i in ans:
    stdout.write(str(i)+" ")