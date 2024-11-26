#<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
#<p>What is the largest prime factor of the number 600851475143?</p>

# solving using basic logic
import time
start = time.time()

def check_prime(x):
    if all(x % i != 0 for i in range(2,x)):
        return True
    else:
        return False


def listprime(list_prime):
    x = int(list_prime[-1])
    
    if check_prime(x):
        return list_prime
    else:
        for i in range(2,x):
            if check_prime(i):
                if x % i == 0:
                    x = int(x/i)
                    list_prime = list_prime[:-1]+[i]+[x]
                    
                    if x == 1:
                        return list_prime
                    else:
                        listprime(list_prime)

print(listprime([10]))
end = time.time()
print(end - start)

# trying to reduce time
import math   
start = time.time()

# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
    list1 = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        list1.append(2) 
        n = n / 2
         
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
        # while i divides n , print i and divide n 
        while n % i== 0: 
            list1.append(i)
            n = n / i 
    # Condition if n is a prime 
    # number greater than 2 
    return list1

print(primeFactors(600851475143))
end = time.time()
print(end - start)
