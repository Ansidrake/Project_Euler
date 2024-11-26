import time 
start =time.time()
print(start)
def rec(x,count=0):
    while x!=1:
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x+1
        count+=1
    return count+1
#print(rec(10000001))
max = 0
for i in range(800000,1000001):
    if rec(i)>max:
        print(i)
        max = rec(i)
print(max)
end = time.time()
print(end-start)