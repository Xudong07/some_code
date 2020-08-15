def num_of_sches_top_down(n, r):
    if n==1:
        return 1
    else:
        if r[n-1] > 0:
            return r[n-1]
        q = 0
        for i in range(n-1):
            q = q + num_of_sches_top_down(i+1, r)*num_of_sches_top_down(n-i-1, r)
        r[n-1] = q
        return r[n-1]


def num_of_sches_bottom_up(n):
    r = [0]*n
    r[0] = 1
    #明确求解顺序，保证后面求解时，需要的子问题都已经解决
    for i in range(1,n):
        for j in range(i):
            r[i] = r[i] + r[i-j-1]*r[j]
    return r

n = 10
r = [0] * n
print(num_of_sches_top_down(n,r))
print(num_of_sches_bottom_up(n))




def matrix_order(p):
    n = len(p)-1
    #构造二维矩阵
    r = [[0 for _ in range(n)] for _ in range(n)]
    m = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(1,n):
        for j in range(n-i):
            finj = i+j  
            m[j][finj] = -1
            for k in range(j, finj):
                q = r[j][k]+r[k+1][finj]+p[j]*p[k+1]*p[finj+1]
                if r[j][finj] == 0:
                    r[j][finj] = q
                    m[j][finj] = k+1
                if q < r[j][finj]:
                    r[j][finj] = q
                    m[j][finj] = k+1
    return r, m


p=[30,35,15,5,10,20,25]
print(matrix_order(p))
                    








