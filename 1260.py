n, l, s = map(int, input().split())

a = [[0]*(n+1) for i in range(n+1)]
visited = [False]*(n+1)

for _ in range(l):
    i, j = map(int, input().split())
    a[i][j] = 1
    a[j][i] = 1

def dfs(s): 
    visited[s] = True
    print(s, end=" ")
    for i in range(1, n+1):
        if not visited[i] and a[s][i] == 1:
            dfs(i)
            
def bfs(s):
    que = [s]
    visited[s] = False
    while que:
        v = que.pop(0)
        print(v, end=" ")
        for i in range(1, n+1):
            if visited[i] and a[v][i] == 1:
                visited[i] = False
                que.append(i)

dfs(s)
print()
bfs(s)
