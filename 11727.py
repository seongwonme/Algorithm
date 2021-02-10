n = int(input())
d = [0, 1, 3, 5]

for i in range(4, n+1):
    if i%2==0:
        d.append(d[i-1]*2+1)    
    else:
        d.append(d[i-1]*2-1)
    

print(d[n]%10007)
