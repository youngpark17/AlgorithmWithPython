import sys
dx = [-1,0,0,1]
dy = [0,-1,1,0]

n,m = map(int,sys.stdin.readline().split())
arr = []

memo = [[-1 for i in range (0,m)] for j in range(0,n)]

for i in range(0,n):
    tmp = list(map(int,sys.stdin.readline().split()))
    arr.append(tmp)

def dfs(k,a,b):
    tmp=0
    if a==n-1 and b==m-1:
        return 1
    else:
        for i in range(0,4):
            nx = a+dx[i]
            ny = b+dy[i]
            if(nx>=0 and ny>=0 and nx<n and ny<m):
                if arr[nx][ny]<k:
                    if memo[nx][ny] == -1:
                     tmp+=dfs(arr[nx][ny],nx,ny)
                    else: tmp+=memo[nx][ny]

        if(tmp==0):
            memo[a][b]=0
        else:
            memo[a][b] = tmp
        return memo[a][b]


dfs(arr[0][0],0,0)
print(memo[0][0])



