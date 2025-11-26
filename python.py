# basiscs of python........

print("hello world")
print("welcome to my channel")
'''
#single line and multiple line comments
welcome to my channel
'''
#variable declaration........

a=23
type(a)
print(a)
c="navin"
type(c)
first_name='navin'
print(first_name)
r=99
print(r+33)
t=19.0
print(type(t))
float(a)

##Boolean........

a1=True
b1=False
type(a1)
type(b1)
a1 & b1
a1 or b1

#strings.......

name1='nabin'
print(name1)
print(type(name1))

#concat.......

name1+'dhakal'
name1+str(a)

#complex numbers.....

j=1.0-2.3j
print(j.real,j.imag)

#Dynamic typing......

a=10
a='krish'
print(a)
a=99
print(a)

first_name="nabin"
last_name="dhakal"
print("My first name is {b} and last name is {a}".format(b=first_name,a=last_name))


#input typecasting........

a=input("Enter the first number")
b=input("Enter the second number")
print(a+b)            #concat
print(int(a)+int(b))  #add  
print(int(a)-int(b))  #sub

 # python Control Flows
 #if statement
val=input("Enter the number")
value_float=float(val)
if(value_float>100):
 print("the number is greater than 100")
else:
 print("the number is smaller than 100")
 
 val1=input("enter any number")
 value_float=float(val1)
 if(value_float%2==0):
  print("the number is even")
 else:
  print("the number is odd")

  #Age form
 
age=float(input("Enter the age"))
if(age<18 and age>1):
   print("Minor Age")
elif(age>=18 and age<=45):
    print("Middle Age")
elif(age<1):
    print("Invalid Age")
else:
    print("Senior Citizen")

#nested if else()......

age=float(input("Enter the age"))
if(age<18 and age>1):
   print("Minor Age")
   if(age<15):
       print("you are in school")
   else:
       print("you are in college")
elif(age>=18 and age<=45):
    print("Middle Age")
elif(age<1):
    print("Invalid Age")
else:
    print("Senior Citizen")
    
#Loops()........
##for loop,while loop

lst=[1,2,3,4,5,6,7]
for i in lst:
     print(i**2)
    
#find the sum of all the elements in the list.......

lst=[1,2,3,4,5,6,7]
sum1=0
for i in lst:
    sum1=sum1+i
print(sum1)

#find the sum of even and odd number........

lst=[1,2,3,4,5,6,7]
even_sum=0
odd_sum=0
for i in lst:
    if(i%2==0):
      even_sum=even_sum+i
    else:
      odd_sum=odd_sum+i
print("Even sum is {}".format(even_sum))
print("odd sum is {}".format(odd_sum))

##while condition........

i=0
even_sum=0
odd_sum=0
while(i<=10):
        if(i%2==0):
          even_sum=even_sum+i
        else:
          odd_sum=odd_sum+i
        i=i+1
print(even_sum,odd_sum)
    
#break.......using break the statement is break from that value(it will not print the value next to it)

x=1
while(x<7):
    print(x)
    if x==4:
        break
    x=x+1
 
#Continue.......continue means skipping that statement where the condtion of continue is applied.....
x=0
while(x<7):
    x=x+1
    if x==4:
        continue
    print(x)
    
#PYTHON OPERATORS.........

#logical operators........
a=True
b=False
True and False
True or  False
not True
not False

#age problems.....

age=int(input("Enter the age"))
if(age>18 and age<=35):
    print("Selected Age group")
elif(age>35):
    print("Senior Citizen")
else:
    print("Minor Age")
    
#Equality Operators.......

a="Nabin"
b="Nabin"
a==b

age=int(input("Enter the age"))
if age==18:
    print("You are eligible for voting in Election")

c="Nabin1"
d="Nabin3"
c==d
    
#memory finding......

a="Nabin"
b="Nabin"
print(id(a))
print(id(b))
a is b 
# is channge is it pointing to the same memory location or not.

lst=["1,2,3"]
lsdt1=["1,2,3"]
print(id(lst))
print(id(lsdt1))
# when collection is created then its object is created differently even though the values are same....

lst is lsdt1 # it will always print false as it is checking same memory.
lst == lsdt1 # it will always print true as it is checking  same values or not.

# comparison.......

marks = float(input("Enter the marks"))
if marks>=35:
    print("Pass")
    if marks>=50 and marks<=70:
     print("first")
elif marks<35 and marks>1:
    print("Fail")
else:
    print("Invalid input")
    
#Arithmetic Operators......
34+56
56-90
46/55
48//5  # // is known as integer divison it gives only whole number...
48%5   # % is used for remainder purpose.....










