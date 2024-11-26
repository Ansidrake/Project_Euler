def check_prime(x):
    if all(x % i != 0 for i in range(2,x)):
        return True
    else:
        return False
i = 3
sum = 2
while i < 2000000:
    for x in range(3, int(i ** 0.5) + 1, 2):
        if i % x == 0:
            break
    else:  # no break
        
        sum += i
    i+=2
print(sum)