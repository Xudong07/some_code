from math import sqrt
try:
    def is_special_num(num):
        potential_set = ['1','3','7','9']
        stri = str(num)
        num3 = sum([int(j) for j in stri])
        if stri[-1] not in potential_set or stri[0] not in potential_set:
            return False
        elif num3%3==0:
            return False
        else:
            leni = len(stri)
            for i in range(leni//2+1):
                if stri[i] != stri[leni-1-i]:
                    return False
            midnum = int(sqrt(num))
            for j in range(2,midnum+2):
                if num%j==0:
                    return False
            return True


    while(True):
        num = input().split()
        num = [int(i) for i in num]
        a,b=num[0],num[1]
        c,d=a//10,b//10
        sumv = 0
        for i in range(c,d+1):
            if is_special_num(i):
                sumv +=1
        print(sumv*10)
except:
    pass

