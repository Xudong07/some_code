# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        maxmul = list(range(1,number+1))
        print maxmul
        for i in range(3, number):
            for j in range(i/2+1):
                tmp = maxmul[j]*maxmul[i-j-1]
                if(tmp>maxmul[i]):
                    maxmul[i] = tmp
            print i, maxmul[i]
        print maxmul
        return maxmul[-1]


a = Solution()
print a.cutRope(15)