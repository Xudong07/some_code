import heapq

def myheapq(data):
    heapq.heapify(data)
    result = [0 for _ in range(len(data))]
    for i in range(len(data)):
        result[i] = heapq.heappop(data)
    return result
    

data = input().split()
data = [int(i) for i in data]
print(data)
result = myheapq(data)
print(result)