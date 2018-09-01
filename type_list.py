l = ['magical unicorns',19,'hello',98.98,'world']
#l = [2,3,1,7,4,12]
#l = ['magical','unicorns']

sum = 0
strcount = 0
intcount = 0
floatcount = 0
string = ""

# check for data type
for i in l:
    if type(i) is int:
        intcount += 1
        sum += i
    elif type(i) is str:
        strcount += 1
        string += i + " "
    elif type(i) is float:
        floatcount += 1
        sum += i

if intcount >= 1 and strcount == 0 and floatcount == 0:
    print "The list you entered is of integer type"
    print "Sum:", sum
elif intcount == 0 and strcount >= 1 and floatcount == 0:
    print "The list you entered is of string type"
    print "String:", string
elif intcount >= 1 or floatcount >= 1 or strcount >= 1:
    print "The list you entered is of mixed type"
    print "String:", string
    print "Sum:", sum

# this program does not test for list data types