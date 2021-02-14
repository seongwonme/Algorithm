from math import gcd
import itertools
import sys

n = int(sys.stdin.readline().rstrip())
a = []

for _ in range(n):
    hap = 0
    a = list(map(int, sys.stdin.readline().split()))
    
    for i, j in itertools.combinations(a[1:], 2):
        hap += gcd(i, j)
    print(hap)
