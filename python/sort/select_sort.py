def select_sort(data):
    for i in range(len(data)-1):
        minv = data[i]
        min_index = i
        for j in  range(i+1, len(data)):
            if data[j]<minv:
                min_index = j
                minv = data[j]
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
    



data = input().split()
data = [int(i) for i in data]
print(data)
select_sort(data)
print(data)