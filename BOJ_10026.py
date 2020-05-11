from sys import stdin
import sys
sys.setrecursionlimit(5000)

n = int(stdin.readline())
graph = [[j for j in list(stdin.readline().rstrip())] for i in range(n)]
visited = [[False for i in range(n)] for j in range(n)]
dx = [-1,0,0,1]
dy = [0,1,-1,0]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            graph[i][j]= 1
        elif graph[i][j]=='G':
            graph[i][j]= 2
        else :
            graph[i][j]==100

def dfs(x,y,color):
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(nx>=0 and ny>=0 and nx<n and ny<n):
            if(graph[nx][ny]==color and not visited[nx][ny]):
                dfs(nx,ny,color)

cnt=0
for i in range(n):
    for j in range(n):
        if(not visited[i][j]):
            cnt+=1
            dfs(i,j,graph[i][j])

print(str(cnt), end=' ')

visited = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if(graph[i][j]==1):
            graph[i][j]=2

cnt=0
for i in range(n):
    for j in range(n):
        if(not visited[i][j]):
            cnt+=1
            dfs(i,j,graph[i][j])

print(cnt)