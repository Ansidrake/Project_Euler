import time
import math
start = time.time()
primes_below_20 = [2, 3, 5, 7, 11, 13, 17, 19]

def check_prime(x):
    if all(x % i != 0 for i in range(2,x)):
        return True
    else:
        return False



def prime(n):
    dict1 = {str(float(l)):1 for l in primes_below_20}
    for i in range(1,21):
        for k in range(1,i):
            x = i ** (1/k)
            print(x)
            if str(float(x)) in dict1:
                print("yes")
                dict1[str(float(x))] = k
    highest = []
    for d in dict1:
        x = dict1[d]
        d = int(float(d)) 
        highest.append(d**x)
    prod = 1
    for i in highest:
        prod *= i
    return prod
print(prime(10))
end = time.time()
print(end - start)