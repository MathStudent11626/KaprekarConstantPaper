def kaprekar(digit): #The Kaprekar Function will give you all the constants for all nth digit numbers (available only for 1 to 10 digit numbers, but can easily be modified)
    constants = [] #List to hold the constants
    if digit == 1: #n = 1
        for i in range(0, 10): #All possible 1 digit numbers (Starts at 0, ends at 10-1 = 9)
            number = str(i) #Converted to string (needed for string concatenation)
            for j in range(40): #Kaprekar's process will be used 40 times to make sure it converges
                a = number[0] #Digit 1
                digits = [a] #A list of all the digits (in this case, there is only one digit)
                greatlist = sorted(digits, reverse=True) #This sorts all of the digits from greatest to least (because there is only one digits, it is the same as the original number)
                great = greatlist[0] #Same thing
                leastlist = sorted(digits) #This sorts all of the digits from least to greatest (because there is only one digits, it is the same as the original number)
                least = leastlist[0] #Same thing
                number = str(int(great)-int(least)) #Highest possible digit arrangement - lowest possible digit arrangement
            if number not in constants: #If after all the iterations, it is a number that the computer has not already found, it is added to the list
                constants.append(number)
    elif digit == 2: #Does the same thing for 2 digit numbers (The greatest possible digit arrangement is now different than the lowest possible digit arrangement)
        for i in range(10, 100):
            number = str(i)
            for j in range(40):
                a = number[0]
                if 10 <= int(number) < 100:
                    b = number[1]
                else:
                    b = "0"
                digits = [a, b]
                greatlist = sorted(digits, reverse=True)
                great = greatlist[0] + greatlist[1]
                leastlist = sorted(digits)
                least = leastlist[0] + leastlist[1]
                number = str(int(great)-int(least))
                if number not in constants:
                    constants.append(number)
    elif digit == 3: #Does the same thing for 3 digit numbers
        for i in range(100, 1000):
            number = str(i)
            for j in range(40):
                a = number[0]
                if 100 <= int(number) < 1000:
                    b = number[1]
                    c = number[2]
                elif 10 <= int(number) < 100:
                    b = number[1]
                    c = "0"
                else:
                    b = "0"
                    c = "0"
                digits = [a, b, c]
                greatlist = sorted(digits, reverse=True)
                great = greatlist[0] + greatlist[1] + greatlist[2]
                leastlist = sorted(digits)
                least = leastlist[0] + leastlist[1] + leastlist[2]
                number = str(int(great)-int(least))
                if number not in constants:
                    constants.append(number)
    elif digit == 4: #Does the same thing for 4 digit numbers
        for i in range(1000, 10000):
            number = str(i)
            for j in range(40):
                a = number[0]
                if 1000 <= int(number) < 10000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                elif 100 <= int(number) < 1000:
                    b = number[1]
                    c = number[2]
                    d = "0"
                elif 10 <= int(number) < 100:
                    b = number[1]
                    c = "0"
                    d = "0"
                else:
                    b = "0"
                    c = "0"
                    d = "0"
                digits = [a, b, c, d]
                greatlist = sorted(digits, reverse=True)
                great = greatlist[0] + greatlist[1] + greatlist[2] + greatlist[3]
                leastlist = sorted(digits)
                least = leastlist[0] + leastlist[1] + leastlist[2] + leastlist[3]
                number = str(int(great)-int(least))
                if number not in constants:
                    constants.append(number)
    elif digit == 5: #Does the same thing for 5 digit numbers
        for i in range(10000, 100000):
            number = str(i)
            for j in range(40):
                a = number[0]
                if 10000 <= int(number) < 100000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                elif 1000 <= int(number) < 10000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = "0"
                elif 100 <= int(number) < 1000:
                    b = number[1]
                    c = number[2]
                    d = "0"
                    e = "0"
                elif 10 <= int(number) < 100:
                    b = number[1]
                    c = "0"
                    d = "0"
                    e = "0"
                else:
                    b = "0"
                    c = "0"
                    d = "0"
                    e = "0"
                digits = [a, b, c, d, e]
                greatlist = sorted(digits, reverse=True)
                great = greatlist[0] + greatlist[1] + greatlist[2] + greatlist[3] + greatlist[4]
                leastlist = sorted(digits)
                least = leastlist[0] + leastlist[1] + leastlist[2] + leastlist[3] + leastlist[4]
                number = str(int(great)-int(least))
                if number not in constants:
                    constants.append(number)
    elif digit == 6: #Does the same thing for 6 digit numbers
        for i in range(100000, 1000000):
            number = str(i)
            for j in range(40):
                a = number[0]
                if 100000 <= int(number) < 1000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                elif 10000 <= int(number) < 100000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = "0"
                elif 1000 <= int(number) < 10000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = "0"
                    f = "0"
                elif 100 <= int(number) < 1000:
                    b = number[1]
                    c = number[2]
                    d = "0"
                    e = "0"
                    f = "0"
                elif 10 <= int(number) < 100:
                    b = number[1]
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                else:
                    b = "0"
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                digits = [a, b, c, d, e, f]
                greatlist = sorted(digits, reverse=True)
                great = greatlist[0] + greatlist[1] + greatlist[2] + greatlist[3] + greatlist[4] + greatlist[5]
                leastlist = sorted(digits)
                least = leastlist[0] + leastlist[1] + leastlist[2] + leastlist[3] + leastlist[4] + leastlist[5]
                number = str(int(great)-int(least))
                if number not in constants:
                    constants.append(number)
    elif digit == 7: #Does the same thing for 7 digit numbers
        for i in range(1000000, 10000000):
            number = str(i)
            for j in range(40):
                a = number[0]
                if 1000000 <= int(number) < 10000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                elif 100000 <= int(number) < 1000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = "0"
                elif 10000 <= int(number) < 100000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = "0"
                    g = "0"
                elif 1000 <= int(number) < 10000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = "0"
                    f = "0"
                    g = "0"
                elif 100 <= int(number) < 1000:
                    b = number[1]
                    c = number[2]
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                elif 10 <= int(number) < 100:
                    b = number[1]
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                else:
                    b = "0"
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                digits = [a, b, c, d, e, f, g]
                greatlist = sorted(digits, reverse=True)
                great = greatlist[0] + greatlist[1] + greatlist[2] + greatlist[3] + greatlist[4] + greatlist[5] + greatlist[6]
                leastlist = sorted(digits)
                least = leastlist[0] + leastlist[1] + leastlist[2] + leastlist[3] + leastlist[4] + leastlist[5] + leastlist[6]
                number = str(int(great)-int(least))
                if number not in constants:
                    constants.append(number)
    elif digit == 8: #Does the same thing for 8 digit numbers
        for i in range(10000000, 100000000):
            number = str(i)
            for j in range(40):
                a = number[0]
                if 10000000 <= int(number) < 100000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                    h = number[7]
                elif 1000000 <= int(number) < 10000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                    h = "0"
                elif 100000 <= int(number) < 1000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = "0"
                    h = "0"
                elif 10000 <= int(number) < 100000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = "0"
                    g = "0"
                    h = "0"
                elif 1000 <= int(number) < 10000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                elif 100 <= int(number) < 1000:
                    b = number[1]
                    c = number[2]
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                elif 10 <= int(number) < 100:
                    b = number[1]
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                else:
                    b = "0"
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                digits = [a, b, c, d, e, f, g, h]
                greatlist = sorted(digits, reverse=True)
                great = greatlist[0] + greatlist[1] + greatlist[2] + greatlist[3] + greatlist[4] + greatlist[5] + greatlist[6] + greatlist[7]
                leastlist = sorted(digits)
                least = leastlist[0] + leastlist[1] + leastlist[2] + leastlist[3] + leastlist[4] + leastlist[5] + leastlist[6] + leastlist[7]
                number = str(int(great)-int(least))
                if number not in constants:
                    constants.append(number)
    elif digit == 9: #Does the same thing for 9 digit numbers
        for i in range(100000000, 1000000000):
            number = str(i)
            for j in range(40):
                a = number[0]
                if 100000000 <= int(number) < 1000000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                    h = number[7]
                    k = number[8]
                elif 10000000 <= int(number) < 100000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                    h = number[7]
                    k = "0"
                elif 1000000 <= int(number) < 10000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                    h = "0"
                    k = "0"
                elif 100000 <= int(number) < 1000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = "0"
                    h = "0"
                    k = "0"
                elif 10000 <= int(number) < 100000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                elif 1000 <= int(number) < 10000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                elif 100 <= int(number) < 1000:
                    b = number[1]
                    c = number[2]
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                elif 10 <= int(number) < 100:
                    b = number[1]
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                else:
                    b = "0"
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                digits = [a, b, c, d, e, f, g, h, k] #i and j have already been used
                greatlist = sorted(digits, reverse=True)
                great = greatlist[0] + greatlist[1] + greatlist[2] + greatlist[3] + greatlist[4] + greatlist[5] + greatlist[6] + greatlist[7] + greatlist[8]
                leastlist = sorted(digits)
                least = leastlist[0] + leastlist[1] + leastlist[2] + leastlist[3] + leastlist[4] + leastlist[5] + leastlist[6] + leastlist[7] + leastlist[8]
                number = str(int(great)-int(least))
                if number not in constants:
                    constants.append(number)
    elif digit == 10: #Does the same thing for 10 digit numbers
        for i in range(1000000000, 10000000000):
            number = str(i)
            for j in range(40):
                a = number[0]
                if 1000000000 <= int(number) < 10000000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                    h = number[7]
                    k = number[8]
                    l = number[9]
                elif 100000000 <= int(number) < 1000000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                    h = number[7]
                    k = number[8]
                    l = "0"
                elif 10000000 <= int(number) < 100000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                    h = number[7]
                    k = "0"
                    l = "0"
                elif 1000000 <= int(number) < 10000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = number[6]
                    h = "0"
                    k = "0"
                    l = "0"
                elif 100000 <= int(number) < 1000000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = number[5]
                    g = "0"
                    h = "0"
                    k = "0"
                    l = "0"
                elif 10000 <= int(number) < 100000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = number[4]
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                    l = "0"
                elif 1000 <= int(number) < 10000:
                    b = number[1]
                    c = number[2]
                    d = number[3]
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                    l = "0"
                elif 100 <= int(number) < 1000:
                    b = number[1]
                    c = number[2]
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                    l = "0"
                elif 10 <= int(number) < 100:
                    b = number[1]
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                    l = "0"
                else:
                    b = "0"
                    c = "0"
                    d = "0"
                    e = "0"
                    f = "0"
                    g = "0"
                    h = "0"
                    k = "0"
                    l = "0"
                digits = [a, b, c, d, e, f, g, h, i, j, k, l]
                greatlist = sorted(digits, reverse=True)
                great = greatlist[0] + greatlist[1] + greatlist[2] + greatlist[3] + greatlist[4] + greatlist[5] + greatlist[6] + greatlist[7] + greatlist[8] + greatlist[9]
                leastlist = sorted(digits)
                least = leastlist[0] + leastlist[1] + leastlist[2] + leastlist[3] + leastlist[4] + leastlist[5] + leastlist[6] + leastlist[7] + leastlist[8] + leastlist[9]
                number = str(int(great)-int(least))
                if number not in constants:
                    constants.append(number)
    print("Out of the all "+str(digit)+" digit numbers, there are "+str(len(constants))+" Kaprekar Constants.")
    print("Here is a list of all the Kaprekar Constants: ")
    for i in range(len(constants)):
        print(constants[i]) #This prints the number of Kaprekar Constants for n digit numbers, and the list of all of them
kaprekar(2) #Whatever number n you put in here, it will find all the Kaprekar constants for n digits
