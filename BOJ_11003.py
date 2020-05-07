from sys import stdin, stdout
from collections import deque
n, l = map(int, stdin.readline().split())

arr =list(map(int,stdin.readline().split()))

que = deque()
for i,j in enumerate(arr):
    tmp=(i,j)
    while(len(que)!=0 and que[-1][1]>j):
        que.pop()
    que.append(tmp)
    if(que[0][0]<=i-l):
        que.popleft()
    stdout.write(str(que[0][1])+" ")






