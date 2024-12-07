
maximum = 0 
number = 1

while number < 10:
    value = 1/number
    for i in range(1,100):
        values = value * 10**i
        string = str(values)[:i]
        print(string[:i+1], string[i+2:])
        if string[:i+1] == string[i+2:2*i+1]:
            if i > maximum:
                maximum = i
                print(maximum, number)
    number += 1

print(maximum)

    
