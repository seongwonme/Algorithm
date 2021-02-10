import sys
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

a.sort(key=lambda x: (x[1], x[0]))
for i in a:
    print(i[0], i[1])
