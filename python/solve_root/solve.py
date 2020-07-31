#-*-coding:utf-8-*-


def getCubeRoot(a):
    print(a)
    eps = 1.0e-12
    if(abs(a-0.0)<eps):
        return 0.0
    if(abs(a-1)<eps):
        return 1.0

    if(a>0 and abs(a)>1.0):
        low = 0.0
        up = a 
    elif(a>0 and abs(a)<1.0):
        low = a
        up = 1.0
    elif(a<0 and abs(a)>1.0):
        low = a 
        up = 0.0
    elif(a<0 and abs(a)<1.0):
        low = -1.0
        up = a
    upcube = pow(up,3) - a
    lowcube = pow(low,3) - a
    if(abs(upcube)<eps):
        return up
    elif(abs(lowcube)<eps):
        return low
    while(True):
        mid = (up+low)/2
        midcube = pow(mid,3) - a
        if(abs(midcube)<eps):
            return mid
        else:
            if(midcube*upcube<0):
                low = mid
            else:
                up = mid





a = float(input())
print('{:.1f}'.format(getCubeRoot(a)))
