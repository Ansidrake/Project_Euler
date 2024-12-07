
def fibbonachi(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def check_lenght(n):
    return len(str(fibbonachi(n)))
 
# def main():
    
#     i = 1
#     last = 0
#     # while check_lenght(i) < 1000:
#     #     last = i
#     #     i *= 10
    
#     print(i,last)
for i in range(3000,8000):
    if check_lenght(i) == 1000:
        print(i)
        break
# main()