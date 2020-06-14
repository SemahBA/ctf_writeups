from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


n=[[7,8,9],[12,5,19],[8,13,15],[14,9,11],[50,23,11],[6,7,11],[14,9,11],[15,16,17],[45,46,47],[13,19,23],[11,9,8],[14,9,11],[50,23,11],[4,7,13],[41,75,23],[7,9,16],[39,28,5],[14,9,11],[50,23,11],[39,28,5],[16,13,15]]
a=[[4,3,4],[10,2,6],[4,6,9],[11,5,7],[5,13,6],[5,6,6],[11,5,7],[3,12,6],[3,2,1],[1,4,3],[7,6,3],[11,5,7],[5,13,6],[3,3,11],[28,35,18],[4,3,7],[38,4,1],[11,5,7],[5,13,6],[38,4,1],[15,11,3]]
flag=""
for i in range(len(n)):
	flag+=chr(chinese_remainder(n[i],a[i]))
print flag

