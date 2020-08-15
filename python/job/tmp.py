import random
while(True):
    num = int(input())
    for _ in range(num):
        m = int(input())
        a = input().split()
        a = [int(i) for i in a]
        print(a)
        a.sort()
        print(a)
        print(a[random.randint(0,m)])
