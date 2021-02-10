import sys
N = int(sys.stdin.readline().strip())
a = [int(sys.stdin.readline().strip()) for _ in range(N)]

a.sort()
for i in a:
    print(i)
