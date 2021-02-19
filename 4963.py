import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x, y):
    l[x][y] = 0
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and l[nx][ny] == 1:
            dfs(nx, ny)
            

while True:
    
    l = []            
    cnt = 0 
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    
    for _ in range(h):
        l.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(h):
        for j in range(w):
            if l[i][j] == 1:            
                dfs(i, j)
                cnt += 1
    
    print(cnt)
