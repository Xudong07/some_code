#*-* coding:utf-8 *-*
def Memoized_cut_rod_top_down(num, p):
    #r stores the reward
    #s stores the selection, policy
    r = [-1]*len(p)
    s = [-1]*len(r)
    return Memoized_cut_rod(p,num,r,s), s

def Memoized_cut_rod(p,n,r,s):
    if n == -1:
        return 0
    else:
        if r[n] >= 0:
            return r[n]
        q = -1
        for i in range(n+1):
            tmp = p[i]+Memoized_cut_rod(p,n-i-1,r,s)
            if tmp > q:
                q=tmp
                s[n]=i+1
    r[n] = q
    return r[n]



def bottom_up_cut_rod(n, p):
    #r stores the reward
    #s stores the selection, policy
    r = [0]*len(p)
    s = [0]*len(p)
    for i in range(n+1):
        q = p[i]
        s[i] = i+1
        for j in range(i):
            tmp = p[j] + r[i-j-1]
            if tmp > q:
                q = tmp
                s[i] = j+1
        r[i] = q
    return r[n], s



p = [1,5,8,9,10,17,17,20,24,30]
n = int(input())
print(Memoized_cut_rod_top_down(n-1, p))
print(bottom_up_cut_rod(n-1,p))