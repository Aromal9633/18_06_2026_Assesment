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
