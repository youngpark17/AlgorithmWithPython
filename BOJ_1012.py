from sys import stdin, stdout
import sys
sys.setrecursionlimit(5000)

t = int(stdin.readline())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
count=0
m,n,k=0,0,0
def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(nx>=0 and ny>=0 and nx<n and ny<m):
            if mp[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx,ny)


for i in range(t):
    m, n, k = map(int, stdin.readline().split())
    mp = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(0)
        mp.append(tmp)
    count=0
    while (k != 0):
        k -= 1
        x, y = map(int, stdin.readline().split())
        mp[y][x] = 1
    visited = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(False)
        visited.append(tmp)

    for i in range(n):
        for j in range(m):
            if(mp[i][j]==1 and not visited[i][j]):
                dfs(i,j)
                count+=1

    print(count)





