#缩小增量排序
import math
def shell_sort(data):
    gap = 1
    while(gap<(len(data))//3):
        gap = gap*3+1
    while(gap>0):
        #insert sort with gap
        for j in range(gap,len(data)):
            current = data[j]
            i = j-gap
            while(i>=0 and data[i]>current):
                data[i+gap] = data[i]
                i = i - gap
            data[i+gap] = current
        gap = math.floor(gap/3)



data = input().split()
data = [int(i) for i in data]
print(data)
shell_sort(data)
print(data)