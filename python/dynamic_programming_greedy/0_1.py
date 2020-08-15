def solve_0_1(v, w, c):
    lenv = len(v)
    r = [[0 for _ in range(c+1)] for _ in range(lenv+1)]
    for i in range(1,c+1):
        for j in range(1,lenv+1):
            if(w[j-1]>i):
                r[j][i] = r[j-1][i]
            else:
                r[j][i] = max(r[j-1][i], r[j-1][i-w[j-1]]+v[j-1])
    return r


v=[1,6,22,18,28]
w=[1,2,6,5,7]
print(solve_0_1(v,w,11))







