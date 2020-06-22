import sys


def isHansu(k):
    lst = list(map(int,list(str(k))))
    if len(lst)==1:
        return True
    dif =  lst[1]-lst[0]
    if len(lst)>=3:
        for i in range(1,len(lst)):
            if lst[i]-lst[i-1]!=dif:
                return False

    return True


n = int(sys.stdin.readline())

cnt = 0
for i in range(1,n+1):
    if isHansu(i):
        cnt+=1

print(cnt)