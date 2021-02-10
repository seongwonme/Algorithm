import sys
N = int(input())
a = [ input().split() for _ in range(N)]

a.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in a:
    print(i[0])
