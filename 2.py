memory1 = 2
memory2 = 1
sum = 2
number = 0
while number < 4000000:
    number = memory1 + memory2
    if number % 2 == 0:
        sum += number
    memory1,memory2 = number,memory1
print(sum)