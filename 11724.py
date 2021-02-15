import sys
sys.setrecursionlimit(10000)
n, l = map(int, sys.stdin.readline().split())
a = [[0]*(n+1) for i in range(n+1)]
visited = [False]*(n+1)
count = 0

for _ in range(l):
    i, j = map(int, sys.stdin.readline().split())
    a[i][j] = 1
    a[j][i] = 1


def dfs(s):
    visited[s] = True
    for i in range(1, n+1):
        if a[s][i] == 1 and not visited[i]:
            dfs(i)
            
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1
        
print(count)
