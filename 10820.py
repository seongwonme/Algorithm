import sys
while(True):
    s = sys.stdin.readline().rstrip('\n')
    if not s:
        break
    #소 대 숫 공
    count = [0]*4
    
    for i in s:
        if i.islower():    count[0] +=1
        elif i.isupper():    count[1] +=1
        elif i.isdigit():    count[2] +=1
        elif i.isspace():    count[3] +=1
        
    print(count[0], count[1], count[2], count[3])
