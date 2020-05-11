from sys import stdin
import sys
from collections import deque

n = int(stdin.readline())
graph  = [[j for j in list(map(int,list(stdin.readline().rstrip())))] for i in range(n)]


visited = [[(1<<31)-1 for i in range(n)] for j in range(n)]

dx= [-1,0,0,1]
dy = [0,1,-1,0]
## 시작에서 끝까지 갈때 만나게 되는 검은방(1) 백트래킹?
def bfs(x,y):
    que = deque()
    que.append((x,y,0))
    visited[x][y]=0
    while(len(que)!=0):
        t = que.popleft()
        for i in range(4):
            nx = t[0]+dx[i]
            ny = t[1]+dy[i]
            if(nx>=0 and ny>=0 and nx<n and ny<n):
                if(graph[nx][ny]==0):
                    if (visited[nx][ny] > t[2] + 1):
                        visited[nx][ny] = t[2]+1
                        que.append((nx, ny, t[2] + 1))
                else:
                    if(visited[nx][ny]>t[2]):
                        visited[nx][ny] = t[2]
                        que.append((nx,ny,t[2]))



bfs(0,0)
if(visited[n-1][n-1]==(1<<31)-1):
    print(0)
else:
    print(visited[n-1][n-1])
