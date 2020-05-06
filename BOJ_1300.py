from sys import stdin,stdout

n = int(stdin.readline())
k = int(stdin.readline())


# B[k]값에 대해서 이분탐색하자. 값은 음... n*n*2

# k번쨰 수는 항상 k보다 작거나 같다. 1*1...  1*n 2*1... 2*n 꼴이기 때문에.
s = 1
e = k
mid = (s+e)//2
ans=0
while(s<=e):
    mid = (s+e)//2
    cnt = 0
    for i in range(1,n+1):
        cnt+=min(mid//i,n)

    if cnt<k:
        s=mid+1
    else :
        ans=mid
        e=mid-1

print(ans)