n = int(input())
a = []
result = [0, 1, 2, 4]
for _ in range(n):
    a.append(int(input()))

for j in range(4, 11):
    result.append(result[j-1]+result[j-2]+result[j-3])
    
for i in a:
    print(result[i])
