till_19_words = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
till_19_numbers = [i for i in range(1,20)]
till_90_words = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
till_90_numbers = [i for i in range(2,10)]
till_900_words = [k + 'hundredand' for k in ['one','two','three','four','five','six','seven','eight','nine']]
till_900_numbers = [i for i in range(1,10)]

#print(till_19_numbers,till_90_numbers,till_900_numbers)

#def calculate(n=1,sum=0):
#    #works
#    if n < 20:
#        k = till_19_numbers.index(n)
#        sum += len(till_19_words[k])
#        return (calculate(n+1,sum))
#    
#    #works
#    elif n < 100:
#        #converts the number into string
#        string = str(n)
#        
#        #finds index of first digit and second digit
#        k = till_90_numbers.index(int(string[0]))
#        # if the second digit is 0 directly return form less than 90 words else find the index 
#        if string[1] == '0':
#            sum += len(till_90_words[k])
#            return calculate(n+1,sum)
#        
#        # if not 0 return find index in the less than 20 number(1-9)
#        j = till_19_numbers.index(int(string[1]))
#        sum += len(till_90_words[k]) + len(till_19_words[j])
#        return calculate(n+1,sum)
#    
#    elif n < 1000:
#        string = str(n)
#        
#        # finding index of first number in the list
#        i = till_900_numbers.index(int(string[0]))
#        
#        # directly returning if the next two digits are 0 cases like 300
#        if string[1:] == '00':
#            sum += len(till_900_words[i][:-3])
#            # [:-3] to eliminate -3 which was added in till_900 words
#            return calculate(n+1,sum)
#        
#        #directly returning if the second digit is 0 cases like 302
#        elif string[1] == '0':
#            sum += len(till_19_words[till_19_numbers.index(int(string[2]))]) + len(till_900_words[i])
#            return calculate(n+1,sum)
#        
#        # directly returning if the third digit is 0 
#        elif string[2] == '0':
#            #since 10 is not in till 90 word handle it seperately like 310
#            if string[1] == '1':    
#                sum += len(till_900_words[i]) + len('ten') 
#                return calculate(n+1,sum)
#            
#            # cases like 320
#            sum += len(till_900_words[i]) + len(till_90_words[till_90_numbers.index(int(string[1]))])
#            return calculate(n+1,sum)
#        
#        # general case with no 0's 
#        # since numbers less than 20 are not considered in ten like 316
#        if int(string[1:]) < 20:
#            j = till_19_numbers.index(int(string[1:]))
#            sum += len(till_900_words[i]) + len(till_19_words[j])
#            return calculate(n+1,sum)
#        
#        k = till_90_numbers.index(int(string[1]))
#        j = till_19_numbers.index(int(string[2]))
#        
#        # the most general case 362
#        sum += len(till_90_words[k]) + len(till_19_words[j]) + len(till_900_words[i])
#        return calculate(n+1,sum)
#    
#    # adding 1000
#    else:
#        return sum + len('onethousand')
#print(calculate())


'''Was getting too many recursion errors so implementaion using for loop '''
sum = 0
for n in range(1,1001):
    #works
    if n < 20:
        k = till_19_numbers.index(n)
        sum += len(till_19_words[k])
        print(till_19_words[k])
        continue
    
    #works
    elif n < 100:
        #converts the number into string
        string = str(n)
        
        #finds index of first digit and second digit
        k = till_90_numbers.index(int(string[0]))
        # if the second digit is 0 directly return form less than 90 words else find the index 
        if string[1] == '0':
            sum += len(till_90_words[k])
            print(till_90_words[k])
            continue
        
        # if not 0 return find index in the less than 20 number(1-9)
        j = till_19_numbers.index(int(string[1]))
        sum += len(till_90_words[k]) + len(till_19_words[j])
        print(till_90_words[k]+till_19_words[j])
        continue
    
    elif n < 1000:
        string = str(n)
        
        # finding index of first number in the list
        i = till_900_numbers.index(int(string[0]))
        
        # directly returning if the next two digits are 0 cases like 300
        if string[1:] == '00':
            sum += len(till_900_words[i][:-3])
            print(till_900_words[i][:-3])
            # [:-3] to eliminate -3 which was added in till_900 words
            continue
        
        #directly returning if the second digit is 0 cases like 302
        elif string[1] == '0':
            sum += len(till_19_words[till_19_numbers.index(int(string[2]))]) + len(till_900_words[i])
            print(till_900_words[i]+till_19_words[till_19_numbers.index(int(string[2]))])
            continue
        
        # directly returning if the third digit is 0 
        elif string[2] == '0':
            #since 10 is not in till 90 word handle it seperately like 310
            if string[1] == '1':    
                sum += len(till_900_words[i]) + len('ten') 
                print(till_900_words[i]+'ten')
                continue
            
            # cases like 320
            sum += len(till_900_words[i]) + len(till_90_words[till_90_numbers.index(int(string[1]))])
            print(till_900_words[i]+till_90_words[till_90_numbers.index(int(string[1]))])
            continue
        
        # general case with no 0's 
        # since numbers less than 20 are not considered in ten like 316
        if int(string[1:]) < 20:
            j = till_19_numbers.index(int(string[1:]))
            sum += len(till_900_words[i]) + len(till_19_words[j])
            print(till_900_words[i]+till_19_words[j])
            continue
        
        k = till_90_numbers.index(int(string[1]))
        j = till_19_numbers.index(int(string[2]))
        
        # the most general case 362
        sum += len(till_90_words[k]) + len(till_19_words[j]) + len(till_900_words[i])
        print(till_900_words[i] + till_90_words[k]+till_19_words[j])
        continue
    
    # adding 1000
    else:
        sum += len('onethousand')
        print('onethousand')
print(sum)





