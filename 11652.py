import sys
n = int(sys.stdin.readline().rstrip())
dic = {}

for _ in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

a = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
print(a[0][0])
