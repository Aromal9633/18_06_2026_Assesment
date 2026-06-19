#Perform Basic Tuple Operations

tuple1=(1,2,3,4,5)

print(tuple1[0])
print(tuple1[:-1])
print(tuple1[::-1])

print(20 in tuple1)
print(4 in tuple1)

print(tuple1)

#Tuple Repetition

tuple1=(1,2,3,4)
result=tuple1*4
print(result)

#Slicing Tuples

tuple1=(1,2,3,4,5,6,7)
result=tuple1[1:5]
print(result)

#Reverse the tuple

tuple1=(1,2,3,4,5,6,7)
result=tuple1[::-1]
print("Reverse of tuple1:",result)

#Access Nested Tuples

tuple1=((1,2,3,4),(5,6,7,8,9))
merge=tuple1[0]+tuple1[1]

print(merge)


#Create a tuple with single item 50

tuple1=(50,)
print(tuple1)

#Unpack the tuple into 4 variables

tuple1=(1,2,3,4)
a,b,c,d=tuple1
print(a)
print(b)
print(c)
print(d)

#Swap two tuples in Python


t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1, t2 = t2, t1
print("t1:", t1)
print("t2:", t2)


#Copy Specific Elements From Tuple


t = (10, 20, 30, 40, 50)

new_t = (t[1], t[3])

print(new_t)

#List to Tuple

list1=[1,2,3,4,5,6]
tuple_list=tuple(list1)
print(tuple_list)

#Remove Items From Set Simultaneously


s = {1, 2, 3, 4, 5}
remove_items = {2, 4}

s.difference_update(remove_items)
print(s)

#Check Subset

set1 = {1, 2,3,4,5}
set2 = {1, 2, 3, 4}

print(set2.issubset(set1))

#Check Superset


set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1.issuperset(set2))

#Set Symmetric Difference Update


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.symmetric_difference_update(set2)
print(set1)




