from sys import stdin, stdout
from collections import deque
n,m = map(int,stdin.readline().split())
lst = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

def bfs():
    for i in range(1,n+1):
        visited[i] = False
    que = deque([])
    visited[f] = True
    que.appendleft(f)

    while(len(que)!=0):
        node = que.popleft()
        if(node==t):
            return True
        for next,value in lst[node]:
            if (visited[next] == False) and (value>=mid):
                visited[next] = True
                que.appendleft(next)
    return False

## 파라메트릭 서치로 20억 부터 찾자
for i in range(0,m):
    a,b,c, = map(int,stdin.readline().split())
    lst[a].append((b,c))
    lst[b].append((a,c))

##다리니까 양방향 그래프.

f,t = map(int,stdin.readline().split())
start = 0
end = 2_000_000_000
mid = 0
while(start!=end):
    mid = (start+end)//2
    flag = bfs()
    if flag:
        start = mid+1
    else:
        end = mid

print(start-1)

