                            #Perform Basic set operations in Python

s={1,2,3,4,5,6,7}
print("Items in the set is:",s)

#Adding elements to Sets

s={1,2,3,4}
s.add(5)

print(s)

#Updating Sets
s={1,2,3,4}
s.update([5,6,7])
print(s)


#removing elements in Sets
s={1,2,3,4,5,6}
s.remove(6)
print(s)


#pop

s={1,2,3,4,5,6}
s.pop()
print(s)


#popitem
s={1,2,3,4,5,6}
s.clear()
print("Output is :",s)


                               #SET OPERATIONS
#Union operations in set
a={1,2,3,4}
b={5,6,7,8}
print(a.union(b))

#Intersection
a={1,2,3,4}
b={5,6,7,8,3,4}
print("Intersection Output:",a.intersection(b))

#Difference
a={1,2,3,4}
b={5,6,7,8}
print("Difference",b-a)

#Remove duplicates


nums = [1, 2, 2, 3, 4, 4]
unique_nums = set(nums)
print(unique_nums)

#Symetric Difference

a={1,2,3,4}
b={2,3,4,5}
print(a^b)
print(a.symmetric_difference(b))

#Add list of elements to a set

a={1,2}
lst=[3,4,5,6]
a.update(lst)
print(a)

#Set Differnce update

a={1,2,7,8}
b={5,6,7,8}

a.difference_update(b)
print("Set Difference Update is:",a)


#Remove Items from Sets Simultenoulsy

a={1,2,3,4,5,6,7,8,9,10}
a.difference_update({5,6,7})
#a.remove(5)
print(a)


#Check Subset

a={1,2,3}
b={1,2,3,4,5,6,7}
print(a.issubset(b))

#Check superset

a={1,2,3,4,5,6,7}
b={1,2,3}
print(a.issuperset(b))
 

#Check Intersection

a={1,2,3,7}
b={1,2,3,4,5,6,7}
print(a.intersection(b))

#Set Symmetric Difference Update

a={1,2,3,4,5,6,7}
b={1,2,3}
a.symmetric_difference_update(b)
print("Symmetric Difference",a)


#Set Intersection Update


a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6, 7}
a.intersection_update(b)
print("Intersection Update",a)

#Find Common elements in two lists

a={1,2,3,4,5}
b={5,6,7,4,10,11,12}
c=a&b
print(c)

#Frozen Set

fs=frozenset([1,2,3,4,5,6])
print(fs)

#Count Unique Words

text = "python is easy and python is powerful"
words=text.split()
unique=set(words)
count=len(unique)
print("Count of Unique Words is:",count)


a={1,2,1,2,3,2,1,3,4,5,6}
print(set(a))