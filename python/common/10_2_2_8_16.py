def trans(num,base):
    data=[]
    while(num!=0):
        data.append(num%base)
        num = num//base
    data.reverse()
    data = [str(i) for i in data]
    data1 = ''.join(data)
    return data1

try:
    while(True):
        num = input()
        if not num:
            break
        num = int(num)
        print(trans(num,2))
except:
     