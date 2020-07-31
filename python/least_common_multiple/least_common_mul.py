#-*-coding:utf-8 -*-
#二者关系：两个数之积=最小公倍数*最大公约数

def least_mul(a, b, c):
    if(a%b==0):
        return a
    else:
        return least_mul(a+c,b,c)





num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])
if num[0]>= num[1]:
    print(least_mul(num[0], num[1], num[0]))
else:
    print(least_mul(num[1], num[0], num[1]))



a  = num[0]
b = num[1]
s = a*b
while a%b!=0:
    a, b = b, (a%b)
print(b)
print(s//b)




