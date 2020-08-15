def recursive_activity(s, f, k, n):
    m = k+1
    while m<n and s[m] < f[k]:
        m = m+1
        print(m)
    if m<n:
        return [k+1]+recursive_activity(s,f,m,n)
    else:
        return [k+1]


info = [(1,4),(12,16),(3,5),(2,14),(0,6),(5,7),(5,9),(3,9),(6,10),(8,11),(8,12)]
info.sort(key=lambda x : (x[1],x[0]))
print(info)
s = [x[0] for x in info]
f = [x[1] for x in info]
print(recursive_activity(s,f,0,len(info)))