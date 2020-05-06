from sys import stdin,stdout

def com(d,c):
    if(c==6):
        for i in range(n):
            if(visited[i] == True):
                stdout.write(str(l[i])+' ')
        stdout.write("\n")
        return
    else:
        for i in range(d,n):
            if(visited[i]==False):
                visited[i] = True
                com(i+1,c+1)
                visited[i]  =False


l = list(map(int,stdin.readline().split()))
n = l[0]
while(n!=0):
    l = l[1:n+1]
    visited = [False]*(n)
    com(0,0)
    stdout.write("\n")
    l = list(map(int, stdin.readline().split()))
    n =l[0]
