# Python Number Methods......

#Absolute Method....# Negative or positive it will always gives absolute values on;y....

a=abs(12)
b=abs(-20)
c=abs(-23)
print(c)
print(a+b+c)
print(b)

d=abs(34.20)
e=abs(-22.09)
print(d)
print(e)

#ceil....# by using it it will always gives ceiling number means next to the number 

import math
a=math.ceil(43.67)
b=math.ceil(43.3)
print(a)
print(b)

math.ceil(42.1)

math.ceil(-44.5)
# cuz minus 44 is greater than 45.......

#floor

math.floor(43.1) #by using it will always gives floor number means lowest to the given number....
r=math.floor(49.9)
print(r)

# exp()....# it will return the exponential value of a number x which we pass in the arguement....

math.exp(10)


#fabs() # it returns positive values.....

b=math.fabs(10.53)
print(b)
y=math.fabs(-19)
print(y)


#log(x)...............

r=math.log(20)
print(r)

e=math.log(65.4)
print(e)

i=math.log10(10)
print(i)

#MAX....it always gives the maximum number.....

o=max(-33,-77,-78,-30)
print(o)
#MIN....it always gives the minimum number.....

z=min(44,56,-90,77,69)
print(z)

#pow...it gives power value of the input number...

import math
a=math.pow(5,6)
print(a)
b=math.pow(9,-2)
print(b)

#sqrt....it gives the sqrt of the input value....

c=math.sqrt(16)
print(c)

d=math.sqrt(81)
print(d)

e=math.sqrt(1221)
print(e)

#Trignometry...

import math
a=math.sin(180)
print(a)
b=math.sin(0)
print(b)
c=math.cos(90)
print(c)
d=math.tan(90)
print(d)

#hypotenese
math.hypot(2,3)

#mods
math.modf(90)

#program to check prime numbers....
#program to check max of 3 numbers....

n=int(input("Enter number: "))
f=[i for i in range(1,n+1) if n%i==0]
print("Factors:",f)
print("Prime" if n>1 and len(f)==2 else "Composite or Neither")

a=40
b=20
c=30
if(a>b and a>c):
    print("a is maximum number")
elif(b>a and b>c):
    print("b is the maximum number")
else:
    print("c is the maximum number")
# from user

a=input("Enter the numbers") # Input as string
a_list=a.split() # Split into list of strings
a_int=[]  # Empty list to hold integers
for num in a_list:
    a_int.append(int(num)) # Convert each to int and append
maximum=a_int[0] # Assume first number is max
for n in a_int:
    if n>maximum:
        maximum=n# after comparing replace the number if it is greater then maximum.....
print("Maximum number is",maximum)
    










