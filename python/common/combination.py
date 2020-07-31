import copy
def combine(lst, l):
    result = []
    tmp = [0] * l
    length = len(lst)
    def next_num(li=0, ni=0):
        if ni == l:
            result.append(copy.copy(tmp))
            return
        for lj in range(li, length):
            tmp[ni] = lst[lj]
            next_num(lj+1, ni+1)
    next_num()
    return result


def permutation(lst,k):
    result = []
    tmp = [0]*k
    def next_num(a,ni=0):
        if ni == k:
            result.append(copy.copy(tmp))
            return
        for lj in a:
            tmp[ni] = lj
            b = a[:]
            b.pop(a.index(lj))
            next_num(b,ni+1)
    #c = lst[:]
    next_num(lst,0)
    return result

a = [1,2,3,4]
print(combine(a,2))
print(permutation(a, 2))
print(a)