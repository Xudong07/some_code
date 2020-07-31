import sys
try:
    while(True):
        num = sys.stdin.readline().strip()
        if(not num):
            break
        num = int(num)
        for i in range(num):
            a = sys.stdin.readline().strip()
            a = list(a)
            lena = len(a)
            if(lena==0):
                continue
            numl = lena//8
            modl = lena%8
            for j in range(numl):
                print(''.join(a[j*8:(j+1)*8]))
            if(modl!=0):
                print(''.join(a[-modl:])+'0'*(8-modl))
except:
    pass