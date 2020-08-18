def Merge_Sort_Mine(data):
    #直接利用递归公式写程序
    if len(data)<=1:
        return data
    middle = len(data)//2
    left, right = data[0:middle], data[middle:]
    return merge(Merge_Sort_Mine(left), Merge_Sort_Mine(right))

def merge(l1,l2):
    result = []
    while l1 and l2:
        if l1[0]<=l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))        
    while l1:
        result.append(l1.pop(0))
    while l2:
        result.append(l2.pop(0))
    return result

data = input().split()
data = [int(i) for i in data]
print(data)
data = Merge_Sort_Mine(data)
print(data)