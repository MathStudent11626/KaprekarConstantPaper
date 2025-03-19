#This code finds the number of times a four-digit number goes to 6174 after x amount of iterations.

#Lists for each iteration
alist = []
blist = []
clist = []
dlist = []
elist = []
flist = []
glist = []
hlist = []
ilist = []
jlist = []


for i in range(0, 10000):
    integer = str(i)
    for j in range(10):
        if 1000 <= int(integer) < 10000: #If the integer has four digits
            a = integer[0]
            b = integer[1]
            c = integer[2]
            d = integer[3]
        elif 100 <= int(integer)< 1000: #If the integer has three digits
            a = integer[0]
            b = integer[1]
            c = integer[2]
            d = "0"
        elif 10 <= int(integer)< 100: #If the integer has two digits
            a = integer[0]
            b = integer[1]
            c = "0"
            d = "0"
        elif 0 <= int(integer)< 10: #If the integer has one digit
            a = integer[0]
            b = "0"
            c = "0"
            d = "0"
        list = [a, b, c, d]
        greatest = sorted(list, reverse=True) #The greatest combination
        smallest = sorted(list) #The smallest combination
        great = ""
        small = ""
        for k in range(4):
            #Convert string into numbers
            great += greatest[k]
            small += smallest[k]
        integer = str(int(great)-int(small)) #Update integer
        #Adding it to specific lists based off of iteration
        if j == 0:
            alist.append(integer)
        if j == 1:
            blist.append(integer)
        if j == 2:
            clist.append(integer)
        if j == 3:
            dlist.append(integer)
        if j == 4:
            elist.append(integer)
        if j == 5:
            flist.append(integer)
        if j == 6:
            glist.append(integer)
        if j == 7:
            hlist.append(integer)
        if j == 8:
            ilist.append(integer)
        if j == 9:
            jlist.append(integer)
#The number of numbers that reach 6174 in x amount of iterations.
print("0. 1")
print("1. "+str(alist.count("6174") - 1))
print("2. "+str(blist.count("6174") - alist.count("6174")))
print("3. "+str(clist.count("6174") - blist.count("6174")))
print("4. "+str(dlist.count("6174") - clist.count("6174")))
print("5. "+str(elist.count("6174") - dlist.count("6174")))
print("6. "+str(flist.count("6174") - elist.count("6174")))
print("7. "+str(glist.count("6174") - flist.count("6174")))
print("8. "+str(hlist.count("6174") - glist.count("6174")))
print("9. "+str(ilist.count("6174") - hlist.count("6174")))
print("10. "+str(jlist.count("6174") - ilist.count("6174")))