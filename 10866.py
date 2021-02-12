import sys
from collections import deque 
n = int(input())
deq = deque()

for _ in range(n):
    a = sys.stdin.readline().split()
	
    if a[0] == 'push_front':    
        deq.append(a[1])
    elif a[0] == 'push_back':
        deq.appendleft(a[1])
    elif a[0] == 'pop_front':
        print(deq.pop() if len(deq)!=0 else -1)
    elif a[0] == 'pop_back':
        print(deq.popleft() if len(deq)!=0 else -1)
    elif a[0] == 'size':
        print(len(deq))
    elif a[0] == 'empty':
        print(1 if len(deq)==0 else 0)
    elif a[0] == 'front':
        print(deq[len(deq)-1] if len(deq)!=0 else -1)
    elif a[0] == 'back':
        print(deq[0] if len(deq)!=0 else -1)
