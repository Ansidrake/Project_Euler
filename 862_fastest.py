from functools import lru_cache
from math import factorial
def nCr(n,r):
    if n<0 or n<r:
        return 0
    return factorial(n)//factorial(r)//factorial(n-r)

def solve(N):
    def Combine(res1,res2):
        return (res1[0]+res2[0],res1[1]+res2[1])
    def Multiply(res,w):
        return (res[0]*w,res[1]*w*w)

    @lru_cache(None)
    def solve(idx,lef):
        if idx == 10:
            if lef:
                return (0,0)
            return (1,1)

        res = (0,0)
        for k in range(lef+1):
            res2=solve(idx+1,lef-k)
            ways=nCr(lef,k)
            res=Combine(res,Multiply(res2,ways))
        return res
    res = (0,0)
    for zero in range(N):
        res2=solve(1,N-zero)
        ways=nCr(N-1,zero)
        res=Combine(res,Multiply(res2,ways))
    ans=(res[1]-res[0])//2
    print(N,ans)

solve(18)
# solve(3)
# solve(12)
# solve(100)
# solve(500)