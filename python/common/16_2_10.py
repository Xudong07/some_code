S = []
for i in range(6):
    S.append(chr(ord('A')+i))
n = [i+10 for i in range(6)]
dict_16 = dict(zip(S,n))
print(dict_16)
try:
    while(True):
        num = input()
        if not num:
            break
        num = num[2:]
        sumv = 0
        lenn = len(num)
        for i in range(lenn):
            if num[i] in S:
                sumv = sumv + dict_16[num[i]]*pow(16,lenn-i-1)
            else:
                sumv = sumv + int(num[i])*pow(16, lenn-i-1)
        print(sumv)
except:
    pass