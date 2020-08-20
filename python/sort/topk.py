import heapq

def myheapq(data,k):
    hp = [-x for x in data[:k]]
    heapq.heapify(hp)
    for i in range(k,len(data)):
        if -hp[0] > data[i]:
            heapq.heappop(hp)
            heapq.heappush(hp,-data[i])
    result = [0 for _ in range(k)]
    for i in range(k-1,-1,-1):
        result[i] = heapq.heappop(hp) * -1
    return result
    

data = input().split()
k = 5
data = [int(i) for i in data]
print(data)
result = myheapq(data,k)
print(result)