#<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
#<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>
import time
start = time.time()
def pallineven(x):
    x = str(x)
    mid = int(len(x)/2)
    return x[:mid]==x[:mid-1:-1]

def findcombination():
    for i in range(999*999,10000,-1):
        if pallineven(i):
            for k in range(999,100,-1):
                if i % k == 0 and len(str(int(i/k)))==3:
                    return [i,i/k,k]
end = time.time()
print(end - start)
print(findcombination())