import math
def heap_ify(data,id):
    left = id*2+1
    right = id*2+2
    maxid = id
    maxv = data[id]
    if left<=lend-1 and data[left] > maxv:
        maxid = left
        maxv = data[left]
    if right<=lend-1 and data[right] > maxv:
        maxid = right
        maxv = data[right]
    if maxid == id:
        return
    else:
        data[maxid], data[id] = data[id], data[maxid]   
        heap_ify(data,maxid)

def Heap_Sort(data):
    '''
    sort with heap
    '''
    global lend
    # construct the heap
    lend = len(data)
    last_id = math.floor(lend/2)-1
    for i in range(last_id,-1,-1):
        heap_ify(data,i)    
    # select and heapify
    for i in range(lend-1,0,-1):
        data[i], data[0] = data[0], data[i]
        lend = lend-1
        heap_ify(data,0)
    return

data = input().split()
data = [int(i) for i in data]
print(data)
Heap_Sort(data)
print(data)