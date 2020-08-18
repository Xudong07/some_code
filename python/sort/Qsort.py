import random
def Qsort_Mine(data, beg, end):
    if beg>=end:
        return
    else:
        part_id = partition(data, beg, end)
        Qsort_Mine(data, beg, part_id-1)
        Qsort_Mine(data,part_id+1, end)
    return

def partition(data, beg, end):
    pivot_id = random.randint(beg,end)
    pivot = data[pivot_id]
    data[pivot_id], data[end] = data[end], data[pivot_id]
    index = beg
    for i in range(beg,end):
        if data[i]<pivot:
            data[i], data[index] = data[index],data[i]
            index = index+1
    data[index], data[end] = data[end], data[index]
    return index

data = input().split()
data = [int(i) for i in data]
print(data)
Qsort_Mine(data,0,len(data)-1)
print(data)