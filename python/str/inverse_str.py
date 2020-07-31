a = list(input())
lena = len(a)
half = int((lena/2.0))
for i in range(half):
    mid = a[i]
    changid = lena-i-1
    a[i]=a[changid]
    a[changid] = mid
print(''.join(a))