def Insert_Sort_Mine(data):
    for i in range(1,len(data)):
        current = data[i]
        j = i-1
        while(j>=0 and data[j]>current):
            data[j+1] = data[j]
            j -=1
        data[j+1] = current
    return

data = input().split()
data = [int(i) for i in data]
print(data)
Insert_Sort_Mine(data)
print(data)