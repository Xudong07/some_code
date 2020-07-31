import sys
try:
    while(True):
        a = sys.stdin.readline()
        if(not a):
            break
        a = list(a.lower())

        print(a)
        count = {}
        template = [' ']
        template = template+[chr(i) for i in range(ord('0'), ord('9')+1)]
        template = template+[chr(i) for i in range(ord('a'), ord('z')+1)]
        print(template)
        for i in range(len(a)):
            print(a[i])
            if a[i] not in template:
                continue
            if a[i] not in count.keys():
                count[a[i]] = 1
            else:
                count[a[i]] = count[a[i]] + 1
        finv = sorted(count.items(), key=lambda x: (-x[1],x[0]))
        ls = []
        print(finv)
        for i in range(len(finv)):
            ls = ls + [finv[i][0]]
        print(''.join(ls))
except:
    pass