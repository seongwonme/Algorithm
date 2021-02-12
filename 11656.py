arr = input()
a =[]
for i in range(len(arr)):
    a.append(arr[i:])
a.sort()
for i in a:
    print(i)
