try:
    while(True):
        n = int(input())
        i = 1
        num = 2
        j = 0
        step=[4,1,5]
        while(i<=n):
            i = i + step[j%3]
            j = j+1
            icube = pow(i, 2)
            i_s = str(i)
            if i_s == str(icube)[-len(i_s):]:
                num = num + 1
        print(num)
except:
    pass


            