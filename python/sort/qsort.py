import sys
import random
def partition(data, start, end, flag):
    randid = random.randint(start, end)
    x = data[end]
    data[end] = data[randid]
    data[randid] = x
    x = data[end]
    i = start-1
    for j in range(start, end):
        if(flag==0):
            if(data[j]<=x):
                i = i+1
                midd = data[j]
                data[j] = data[i]
                data[i] = midd
        else:
            if(data[j]>=x):
                i = i+1
                midd = data[j]
                data[j] = data[i]
                data[i] = midd
    midd = data[i+1]
    data[i+1] = data[end]
    data[end] = midd
    return i + 1

def qsort_mine(data, start, end, flag):
    if start<end:
        q = partition(data, start, end, flag)
        qsort_mine(data, start, q-1,flag)
        qsort_mine(data, q+1, end,flag)
    return
    


while(True):
    num = sys.stdin.readline()
    if(not num):
        break
    num = int(num.strip())
    data = input().split()
    #data = sys.stdin.readline().strip().split()
    data = [int(i) for i in data]
    flag = int(sys.stdin.readline().strip())
    qsort_mine(data, 0, len(data)-1,flag)
    for i in data:
        print(i, end=' ')
    print(' ')
