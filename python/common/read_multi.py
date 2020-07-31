import sys
numn = 0
nump = 0
sumv = 0
try:
    while(1):
        num = sys.stdin.readline().strip().split()
        if(not num):
            break
        for i in range(len(num)):
            a = int(num[i])
            if(a<0.0):
                numn = numn+1
            else:
                nump = nump + 1
                sumv = sumv + a    
except:
    pass

print(numn)
if(nump==0):
    print(0.0)
else:
    print('{:.1f}'.format(sumv/nump))