from sys import stdin,stdout
import heapq
n = int(stdin.readline())
heap = []
while(n>0):
    n-=1
    k = int(stdin.readline())
    if k==0:
        if len(heap)==0:
            stdout.write("0\n")
        else:
            stdout.write(str(heapq.heappop(heap))+"\n")
    else:
        heapq.heappush(heap,k)