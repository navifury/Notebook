#SETS.....unordered collection that is iterable,mutuable,and has no duplicate elements.....it is based on a data structure known as hash table...

type({1,2,3,4,5,'krish'})
a=set([1,2,3,3,4,5,6,6,7,8,8,8])
print(a)

#defining a empty set......

set_var=set()
print(set_var)
print(type(set_var))

set_var={1,2,3,5,4,6,7,7,8,6,9}
set_var

set_var={"Avengers","Ironman","HUlk"}
print(set_var)

for i in set_var:
    print(i)
    
#inbuilt function in sets.....

set_var.add("Navin")
set_var
'''
set_1=set([4,2,3,1,6,7])
print(set_1)
set_1.add(0)
print(set_1)
'''
#intersection...

set1={"ironman","hulk","spiderman","thor"}
set2={"captain America","hulk","spiderman","wonda"}
set2.intersection(set1)
set2.intersection_update(set1)
 
#difference....
set8={1,2,3,4,5}
set7={1,2,3}
a=set8.difference(set7)
print(a)

set4={1,2,3,4,5,6,7,8,9}
set5={1,2,3}
b=set4.difference(set5)
print(b)


#dictionaries..a collection which is unordered,changeable and indexed....

type({1:"Nabin"})

dict(name="nabin",age=21,last_name="dhakal")

#let's create a dictionary.....

my_dict={"car1":"Audi","car2":"BMW","car3":"mercidies benz"}
type(my_dict)

#indexing
a=my_dict["car1"]
b=my_dict["car3"]
print(a)
print(b)

my_dict.values()

#we can even loop the dictionaries keys

for x in my_dict:
    print(x)

#loop the values.....

for x in my_dict.values():
    print(x)

for x in my_dict.items():
    print(x)
    
#add items in dict....

my_dict["car4"]="ferrari"
my_dict

#Nested Dictionary......

car1_model={'Mercedes':1960}
car2_model={'Audi':1970}
car3_model={'Ferrari':1980}

car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model}
print(car_type)

print(car_type['car1']['Mercedes'])
print(car_type['car3']['Ferrari'])
print(car_type['car2']['Audi'])

#Tuple.......

b=my_tuple=tuple()
print(b)

a=my_tuple=()
print(a)
type(a)

my_tuple=("Nabin","Dhakal","Nabin","Anish")
print(my_tuple)
print(type(my_tuple))

#inbuilt functions......

my_tuple
my_tuple.count("Nabin")
my_tuple[0]
my_tuple.index("Dhakal")
my_tuple.index("Nabin")
my_tuple.index("Anish")

#typecasting in tuple to set and list.....
list(my_tuple)
set(my_tuple)











