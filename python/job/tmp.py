class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num = [1]
        i2=i3=i5=0
        for i in range(1,n):
            a2 = num[i2]*2
            a3 = num[i3]*3
            a5 = num[i5]*5
            ugly = min([a2,a3,a5])
            num.append(ugly)
            if ugly == a2:
                i2 = i2+1
            if ugly == a3:
                i3 = i3+1
            if ugly == a5:
                i5 = i5+1
            print(i2,i3,i5)
        print(num)
        return num[n-1]

print(Solution().nthUglyNumber(10))