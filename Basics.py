# Python Basics

name = "Awesome the eminem"
a = 10
len(name)
name.count("e")

name.lower()
name.capitalize()
name.upper()
name[1]
name[0:9]
name[0:]

# String conversion
str(9)
str(213)
# Adding strings 
"this "+"is "+"awesome"

# String manipulation 
import re
re.sub("[^A-Za-z]"," ","ada 1231zxdq #@$@zxfsd312")
re.sub("[^A-Za-z0-9]"," ","ada 1231zxdq #@$@zxfsd312")
name.replace("e","FF")
name.endswith("i")
name.isalnum() # checking whether it is string 
name.isalpha()
help(name.isalpha)

name.isnumeric()
name[0]="B" # string does not support assignment operator
# Explore more string functions 

# And, or, not => and, or, not operators for operating between different conditions 

# Loops and Conditional programming 
# if elif else key words
x = [1,2,3,4,5,611,12,1231,0]

for i in x:
    if i==0:
        print ("IDK")
    elif i%2==0:
        print ("even")
    elif not i%2==0:
        print ("odd")
    else:
        print ("Enter any number")
    


# Creating our custom functions - syntax 
        
def sum(i):
    add = 0
    for j in i:
        add = add+j
    print (add)
        
sum([1,2,3,4,5,6,100])
import math
def confirm_prime(i):
    j=2
    if i < 2:
        print ("IDK")
    elif i == 2:
        print ("Yes")
    else:
        j=2
        a = int(math.sqrt(i))
        while (j<a):
            if i%j==0:
                #print ("No")
                break
            else:
                j=j+1
    if j >= int(math.sqrt(i)):
        print("Yes")
    else: print ("NO")

# Enter only whole numbers 
confirm_prime(100)
confirm_prime(120)
confirm_prime(7)
k = [2,3,5,7,11,13,1,100,143,12,17,19,20]
for o in k:
    confirm_prime(o)
    
# type gets you type of data or type of data structure 
# lists and dictionaries 
x = [1,2,3,5,6]
len(x)            
for i in x:
    print (i)

y = [11,12,13,14]
x+y
# list functions
x.append(100)
x.append([101,102,103])
x.extend(   [104,105])
x.index(100)
x.insert(13,200)
2*x 
[2*i for i in x]
x = [1,2,100,10,-5,-20,53,32,23]
x.sort(reverse=False)
x
x.sort(reverse=True)
x
# dictionaries 
x = {"A":1,"B":-12,"C":30,"D":5,"E":120,"F":6,"G":12}
x
x.keys()
x.values()
x["H"] = 100
x
del x["H"]
x
# sorting dictionary 
y = sorted(x.items(),key = lambda p:p[1])
y
y.reverse()
y
if "i" in "this":
    print ("yes")
[i for i in "thisiseawsome" if i not in "i"]
"".join([i for i in "thisiseawsome" if i not in "i"])

# [i for i in x if i%2==0]

######## Numpy ############
import numpy as np
y = np.array(x)
y>10
y**2
y+1
y[y%2==0]

x = [1,2,3,4,5,6]
y = [7,8,9,10,11,12]
z = np.array([x,y]).reshape(2,6)
z[0]
z[0][1]
z.shape
z[:,4:]

# Statistics on numpy array 
np.mean(z)
np.median(z)
np.mean(z[1,:])
np.mean(z[:,1])

np.corrcoef(z[0,:],z[1,:])

# Few functions in numpy 
np.round(1.21312,2)
temp1 = np.random.normal(10,2,20)
temp2 = np.random.normal(-10,2,20)
temp2
temp1
temp3 = np.column_stack((temp1,temp2))
np.random.random((2,2))
